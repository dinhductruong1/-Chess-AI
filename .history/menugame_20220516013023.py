import pygame_menu
from pygame_menu.examples import create_example_window
import pygame_menu.widgets
from typing import Tuple, Any
import main
surface = create_example_window('Cờ vua', (512, 512))


def set_difficulty(selected: Tuple, value: Any) -> None:
    """
    Set the difficulty of the game.
    """
    print(f'Set difficulty to {selected[0]} ({value})')


def set_chess_color(selected: Tuple, value: Any):
    if value == 0:
        main.human_chess_color = True
    else:
        main.human_chess_color = False


def set_bot1(selected: Tuple, value: Any):
    pass


def set_bot2():
    pass


def start_the_game():
    main.human_vs_minimax(True)


menu = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Nhập môn trí tuệ nhân tạo',
    width=512
)

menu.add.dropselect(
    title='Chọn chế độ',
    items=[('Đánh với máy ', 0),
           ('Đánh với máy ', 0),
           ('Máy với máy', 1)],
    default=0,
    font_size=16,
    selection_option_font_size=20,
    onchange=set_difficulty
)
menu.add.dropselect(
    title='Chọn màu cờ',
    items=[('Trắng: đi trước', 0),
           ('Đen: đi sau', 1)],
    default=0,
    font_size=16,
    selection_option_font_size=20,
    onchange=set_chess_color
)
menu.add.dropselect(
    title='Độ khó BOT 1',
    items=[('Dễ', 0),
           ('Trung bình', 1),
           ('Khó', 2), ],
    default=0,
    font_size=16,
    selection_option_font_size=20,
    onchange=set_bot1
)
menu.add.dropselect(
    title='Độ khó BOT 2',
    items=[('Dễ', 0),
           ('Trung bình', 1),
           ('Khó', 2), ],
    default=0,
    font_size=16,
    selection_option_font_size=20,
    onchange=set_bot2
)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)


def cont():
    menu.mainloop(surface)


# cont()
