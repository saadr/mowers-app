import unittest
from mowers.model.models import Position, Mower, Lawn, Instructions, Orientations
from mowers.movement.movement_manager import MovementManager


class TestMovementManager(unittest.TestCase):

    def test_process_instruction(self):
        mower = Mower(10, 10, 'N', [])
        movement_manager = MovementManager(Lawn(20, 20))

        movement_manager.process_instruction(mower, Instructions.L)
        movement_manager.process_instruction(mower, Instructions.F)
        movement_manager.process_instruction(mower, Instructions.F)
        movement_manager.process_instruction(mower, Instructions.L)
        movement_manager.process_instruction(mower, Instructions.F)

        self.assertEqual(vars(mower.position), vars(Position(8, 9)))
        self.assertEqual(mower.orientation, Orientations.S)

    def test_process_mower(self):
        mower_1 = Mower(1, 2, 'N', list('LFLFLFLFF'))
        mower_2 = Mower(3, 3, 'E', list('FFRFFRFRRF'))
        movement_manager = MovementManager(Lawn(5, 5))

        movement_manager.process_mower(mower_1)
        self.assertEqual(vars(mower_1.position), vars(Position(1, 3)))
        self.assertEqual(mower_1.orientation, Orientations.N)

        movement_manager.process_mower(mower_2)
        self.assertEqual(vars(mower_2.position), vars(Position(5, 1)))
        self.assertEqual(mower_2.orientation, Orientations.E)
