from enum import Enum


class Instructions(Enum):
    L = 'L'
    R = 'R'
    F = 'F'


class Orientations(Enum):
    N = 'N'
    E = 'E'
    W = 'W'
    S = 'S'


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Lawn:
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y


class Mower:
    def __init__(self, start_x, start_y, start_orientation, instructions):
        self.position = Position(start_x, start_y)
        self.orientation = Orientations[start_orientation]
        self.instructions = [Instructions[i] for i in instructions]
