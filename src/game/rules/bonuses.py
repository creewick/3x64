from random import choice
from ..models.block import Block
from ..models.bonus import Bonus
from .helpers import is_in_bounds

def anvil(game):
    def place(board, x, y):
        for dy in range(1, 4):
            if is_in_bounds(board, x, y + dy):
                board.xy[y + dy][x] = None
                game.state.score += 1
    game.state.board.next_block = Block.Bonus('anvil', place)

all_bonuses = [
    Bonus('Anvil', anvil)
]

def give_random_bonus(game):
    game.state.bonuses.append(
        choice(all_bonuses)
    )

def use_bonus(game, i):
    if len(game.state.bonuses) <= i:
        return
    game.state.bonuses.pop(i).on_call(game)
