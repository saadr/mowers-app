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


    def test_exceeding_lawer_surface(self):
        # Mower at (5,5) heading to North, on a lawn of 5x5 surface.
        # Instructions : FFFRFRF :
        #   The first 3 forward actions should be cancelled (would lead to position (5,6) )
        #   The next R action should make the mower heading to Est
        #   The next forward action should be canclled too (would lead to position (6,5) )
        #   The next R action should make the mower heading to South, forward actions would be possible then.

        mower = Mower(5, 5, 'N', list('FFFRFRFF'))
        movement_manager = MovementManager(Lawn(5, 5))

        movement_manager.process_mower(mower)
        self.assertEqual(vars(mower.position), vars(Position(5, 3)))
        self.assertEqual(mower.orientation, Orientations.S)

