import concurrent.futures
import logging

import mowers.utils.input_parser as input_parser
from mowers.movement.movement_manager import MovementManager
from mowers.utils.output_generator import OutputGenerator

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

NUM_WORKERS = 2
input_path = 'sample_input.txt'
output_generator = OutputGenerator()


def main():
    try:
        with open(input_path) as f:
            lawn = input_parser.parse_lawn(f.readline())
            handler = MovementManager(lawn)

            with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
                futures_map = {}
                mower_order = 0
                for position_line in f:
                    instruction_line = f.readline()
                    mower = input_parser.parse_mower(position_line, instruction_line, lawn)
                    futures_map[executor.submit(handler.process_mower, mower)] = mower_order
                    mower_order += 1

                completed = 0
                for future in concurrent.futures.as_completed(futures_map):
                    order = futures_map[future]
                    try:
                        (x, y, orientation) = future.result()
                    except Exception as e:
                        log.error('Error occured while getting mower final position ', e)
                    else:
                        output_generator.append_result(x, y, orientation, order)
                        completed += 1
                        if completed == len(futures_map):
                            log.info("All mowers done moving.")
                            output_generator.print_in_order()

    except FileNotFoundError:
        log.error('Specified input file path could not be found')
        return 1
    except Exception as e:
        log.error('Some error occurred', e)
        return 1
    return 0


if __name__ == '__main__':
    main()
