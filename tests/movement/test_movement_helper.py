import unittest
import mowers.movement.movement_helper as movement_helper
from mowers.model.models import Orientations, Position


class TestMovementHelper(unittest.TestCase):
    def test_next_orientation(self):
        self.assertEqual(movement_helper.get_left_orientation(Orientations.N), Orientations.W)
        self.assertEqual(movement_helper.get_right_orientation(Orientations.N), Orientations.E)

        self.assertEqual(movement_helper.get_left_orientation(Orientations.E), Orientations.N)
        self.assertEqual(movement_helper.get_right_orientation(Orientations.E), Orientations.S)

        self.assertEqual(movement_helper.get_left_orientation(Orientations.S), Orientations.E)
        self.assertEqual(movement_helper.get_right_orientation(Orientations.S), Orientations.W)

        self.assertEqual(movement_helper.get_left_orientation(Orientations.W), Orientations.S)
        self.assertEqual(movement_helper.get_right_orientation(Orientations.W), Orientations.N)

    def test_next_position(self):
        position = Position(10, 10)
        pos = movement_helper.get_next_position(position, Orientations.W)
        self.assertEqual(vars(movement_helper.get_next_position(position, Orientations.W)), vars(Position(9, 10)))
        self.assertEqual(vars(movement_helper.get_next_position(position, Orientations.E)), vars(Position(11, 10)))
        self.assertEqual(vars(movement_helper.get_next_position(position, Orientations.S)), vars(Position(10, 9)))
        self.assertEqual(vars(movement_helper.get_next_position(position, Orientations.N)), vars(Position(10, 11)))
