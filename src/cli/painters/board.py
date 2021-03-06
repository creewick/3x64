from .painter import get_block_size, draw_panel, get_palette_by_side

def draw_board_frame(client, screen):
    block = get_block_size(client, screen)
    count = len(client.game.state.board.xy)
    width = 2 * block * count
    left = get_board_left(client, screen)
    top = get_board_top(client, screen)

    draw_panel(screen, get_angles(width), left, top, client.palettes['ui'])
    draw_panel(screen, get_vertical_frame(width//2), left+width+1, top+1, get_palette_by_side(client, 3))
    draw_panel(screen, get_top_frame(width), left+1, top, get_palette_by_side(client, 2))
    draw_panel(screen, get_vertical_frame(width//2), left, top+1, get_palette_by_side(client, 1))
    draw_panel(screen, get_bottom_frame(client, width), left+1, top+width//2+1,get_palette_by_side(client))

def get_top_frame(width):
    return ['═' * width]

def get_bottom_frame(client, width):
    progress = get_progress(client, width)
    frame = '═' * progress + '┄' * (width - progress)
    if client.game.state.board.clockwise:
        return [frame[::-1]]
    return [frame]

def get_vertical_frame(height):
    return ['║' for _ in range(height)]

def get_angles(width):
    return [
            f"╦{' ' * width}╦",
            *["" for _ in range(width // 2)],
            f"╚{' ' * width}╝"
    ]

def get_progress(client, width):
    game = client.game
    return max(0, game.state.board.time_to_rotate) * width // game.settings.max_time_to_rotate

def get_board_left(client, screen):
    y, x = screen.getmaxyx()
    block = get_block_size(client, screen)
    count = len(client.game.state.board.xy)
    return x // 2 - block * count - 1

def get_board_top(client, screen):
    y, x = screen.getmaxyx()
    block = get_block_size(client, screen)
    count = len(client.game.state.board.xy)
    return y // 2 - block * count // 2 - 1
