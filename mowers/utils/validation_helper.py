from mowers.model.models import Orientations, Instructions


def is_valid_direction(orientation):
    return orientation in Orientations.__members__


def is_valid_position(x, y, max_x, max_y):
    return 0 <= x <= max_x and 0 <= y <= max_y


def is_valid_instruction(instruction):
    return instruction in Instructions.__members__
