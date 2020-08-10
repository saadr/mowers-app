from mowers.model.models import Lawn, Mower
from mowers.utils import validation_helper


def parse_lawn(lawn_line):
    surface = list(map(int, split_line(lawn_line)))
    if len(surface) != 2 or surface[0] + surface[1] < 0:
        raise Exception('Input parsing error. Invalid lawn surface specification')

    return Lawn(surface[0], surface[1])


def parse_mower(start_line, instruction_line, lawn):
    start_split = split_line(start_line)
    if len(start_split) != 3:
        raise Exception(f"Input parsing error. Invalid mower specification. Line: {start_line}")

    start_x, start_y = int(start_split[0]), int(start_split[1])
    if not validation_helper.is_valid_position(start_x, start_y, lawn.max_x, lawn.max_y):
        raise Exception(f"Input parsing error. Mower position cannot be outside [(0,0), ({lawn.max_x}, {lawn.max_y})]. Line: {start_line}")

    orientation = start_split[2]
    if not validation_helper.is_valid_direction(orientation):
        raise Exception(f"Input parsing error. Invalid mower orientation. Line: {start_line}")

    return Mower(start_x, start_y, orientation, list(instruction_line.rstrip()))


def split_line(line):
    return line.rstrip().split(' ')
