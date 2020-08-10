import concurrent.futures
import logging

import mowers.util.input_parser as input_parser
from mowers.movement.movement_manager import MovementHandler
from mowers.util.output_generator import OutputGenerator

log = logging.getLogger(__name__)
NUM_WORKERS = 2
input_path = '../tests/resources/input.txt'
output_generator = OutputGenerator()


def main():
    try:
        with open(input_path) as f:
            lawn = input_parser.parse_lawn(f.readline())
            handler = MovementHandler(lawn)

            with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
                futures_map = {}
                output = []
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
                        log.error('Error occured while getting mower final position ' + str(e))
                    else:
                        output_generator.append_result(x, y, orientation, order)
                        completed += 1
                        if completed == len(futures_map):
                            log.info("All mowers done moving.")
                            output_generator.print_in_order()

    except FileNotFoundError:
        log.error('Specified file path could not be found')
        return 1
    except Exception as e:
        print('Some error occurred, ' + str(e))
        return 1
    return 0


if __name__ == '__main__':
    main()
