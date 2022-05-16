import pygame_menu
from pygame_menu.examples import create_example_window
import pygame_menu.widgets
from typing import Tuple, Any
surface = create_example_window('Cờ vua', (512, 512))


def set_difficulty(selected: Tuple, value: Any) -> None:
    """
    Set the difficulty of the game.
    """
    print(f'Set difficulty to {selected[0]} ({value})')


def start_the_game():
    #
    print('Start the game')


menu = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Nhập môn trí tuệ nhân tạo',
    width=512
)

menu.add.dropselect(
    title='Chọn chế độ',
    items=[('Đánh với máy', 0),
           ('Máy với máy', 1)],
    default=0,
    font_size=16,
    selection_option_font_size=20
)

menu.add.dropselect(
    title='Độ khó máy đi trước',
    items=[('Đánh với máy', 0),
           ('Máy với máy', 1)],
    default=0,
    font_size=16,
    selection_option_font_size=20
)
menu.add.dropselect(
    title='Độ khó máy đi sau',
    items=[('Đánh với máy', 0),
           ('Máy với máy', 1)],
    default=0,
    font_size=16,
    selection_option_font_size=20
)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
