from __future__ import with_statement

import logging
import threading

import mowers.movement.movement_helper as movement_helper
import mowers.util.validation_helper as validation_helper
from mowers.model.models import Lawn, Mower, Instructions

log = logging.getLogger(__name__)


class MovementHandler:
    def __init__(self, lawn: Lawn):
        if lawn is None:
            raise Exception("Lawn should not be None.")

        self.lawn = lawn
        self.occupied_positions = []
        self.lock = threading.Lock()

    def process_mower(self, mower: Mower):
        if mower is None:
            raise Exception("Mower should not be None.")

        with self.lock:
            self.occupied_positions.append(mower.position)

        for instruction in mower.instructions:
            self.process_instruction(mower, instruction)

        return mower.position.x, mower.position.y, mower.orientation.value

    def process_instruction(self, mower: Mower, instruction: Instructions):
        if instruction == Instructions.L:
            mower.orientation = movement_helper.get_left_orientation(mower.orientation)
        elif instruction == Instructions.R:
            mower.orientation = movement_helper.get_right_orientation(mower.orientation)
        elif instruction == Instructions.F:
            self.process_forward_movement(mower)

    def process_forward_movement(self, mower: Mower):
        next_position = movement_helper.get_next_position(mower.position, mower.orientation)

        if not validation_helper.is_valid_position(next_position.x, next_position.y, self.lawn.max_x, self.lawn.max_y):
            log.info(f"Cancelling movement exceeding lawn surface. Position :({next_position.x}, {next_position.y})")
            return mower.position

        with self.lock:
            if next_position in self.occupied_positions:
                log.info(f"Cancelling movement that would cause mowers overlap. Position :({next_position.x}, {next_position.y})")
                return mower.position

            self.update_occupied_position(mower.position, next_position)
            mower.position = next_position

    def update_occupied_position(self, position, new_position):
        if position in self.occupied_positions:
            self.occupied_positions[self.occupied_positions.index(position)] = new_position
        else:
            self.occupied_positions.append(new_position)
