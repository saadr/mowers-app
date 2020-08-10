import concurrent.futures
import logging

import mowers.input_parser as input_parser
from mowers.movement_manager import MovementHandler

log = logging.getLogger(__name__)
NUM_WORKERS = 2


def main():
    path = '../tests/resources/input.txt'
    try:
        with open(path) as f:
            lawn = input_parser.parse_lawn(f.readline())
            handler = MovementHandler(lawn)

            with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
                for position_line in f:
                    instruction_line = f.readline()
                    mower = input_parser.parse_mower(position_line, instruction_line, lawn)
                    executor.submit(handler.process_mower(mower))

    except FileNotFoundError:
        log.error('Specified file path could not be found')
        return 1
    except Exception as e:
        print('Some error occurred, ' + str(e))
        return 1
    return 0


if __name__ == '__main__':
    main()
