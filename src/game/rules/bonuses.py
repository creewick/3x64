from random import choice
from ..models.block import Block
from ..models.bonus import Bonus
from .helpers import is_in_bounds
from .gravity import pull_down

def anvil(game):
    def place(board, x, y):
        count = 0
        for dy in range(1, 4):
            if is_in_bounds(board, x, y + dy):
                board.xy[y + dy][x] = None
                count += 1
        game.state.score += count
        game.state.last_event = (game.state.play_time, f'+ {count}')
    game.state.board.next_block = Block.Bonus('anvil', place)

def change_direction(game):
    game.state.board.time_to_rotate = min(
        game.settings.max_time_to_rotate,
        game.settings.max_time_to_rotate - game.state.board.time_to_rotate
    )
    game.state.board.clockwise = not game.state.board.clockwise

def remove_line(game):
    blocks = [block for block in game.state.board.xy[-1] if block is not None]
    game.state.board.xy[-1] = [None for _ in range(len(game.state.board.xy))]
    pull_down(game)
    game.state.score += len(blocks)
    game.state.last_event = (game.state.play_time, f'+ {len(blocks)}')

all_bonuses = [
    Bonus('Anvil', anvil),
    Bonus('Change Dir.', change_direction),
    Bonus('Remove Line', remove_line)
]

def give_random_bonus(game):
    if len(game.state.bonuses) < 3:
        game.state.bonuses.append(
            choice(all_bonuses)
        )
        game.state.last_event = (game.state.play_time, f'+ {game.state.bonuses[-1].name}')
    else:
        game.state.score += 10
        game.state.last_event = (game.state.play_time, '+10')

def use_bonus(game, i):
    if len(game.state.bonuses) <= i:
        return
    game.state.last_event = (game.state.play_time, f'- {game.state.bonuses[i].name}')
    game.state.bonuses.pop(i).on_call(game)
