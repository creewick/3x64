from __future__ import annotations
from .settings import Settings
from .block import Block

class Board:
    def __init__(self, xy: [[Block]], cur_block: Block, next_block: Block,
                 cur_pos: (int,int), sides: [int], clockwise: bool):
        self.xy         : [[Block]] = xy
        self.cur_block  : Block     = cur_block
        self.next_block : Block     = next_block
        self.cur_pos    : (int,int) = cur_pos
        self.sides      : [int]     = sides
        self.clockwise  : bool      = clockwise

    @staticmethod
    def New_Game(settings: Settings) -> Board:
        size = settings.size
        return Board(
            xy         = [[None for x in range(size)]
                                for y in range(size)],
            cur_block  = None,
            next_block = None,
            cur_pos    = None,
            sides      = [0, 1, 2, 3],
            clockwise  = False
        )
