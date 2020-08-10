from mowers.models import Position, Orientations


def get_left_orientation(orientation: Orientations):
    if orientation == Orientations.N:
        return Orientations.W
    elif orientation == Orientations.W:
        return Orientations.S
    elif orientation == Orientations.S:
        return Orientations.E
    elif orientation == Orientations.E:
        return Orientations.N
    else:
        raise Exception(f"Unknown orientation : {orientation}")


def get_right_orientation(orientation: Orientations):
    if orientation == Orientations.N:
        return Orientations.E
    elif orientation == Orientations.E:
        return Orientations.S
    elif orientation == Orientations.S:
        return Orientations.W
    elif orientation == Orientations.W:
        return Orientations.N
    else:
        raise Exception(f"Unknown orientation : {orientation}")


def get_next_position(position: Position, orientation: Orientations):
    if not position:
        raise Exception("Mower position is None.")

    if orientation == Orientations.N:
        return Position(position.x, position.y + 1)
    elif orientation == Orientations.E:
        return Position(position.x + 1, position.y)
    elif orientation == Orientations.S:
        return Position(position.x, position.y - 1)
    elif orientation == Orientations.W:
        return Position(position.x - 1, position.y)
    else:
        raise Exception(f"Unknown orientation : {orientation}")
