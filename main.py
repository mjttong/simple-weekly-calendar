import flet as ft
from datetime import datetime
import style
from components.title_bar import Title_bar
from components.day_box import Day_box

def main(page: ft.Page):
    # page default settings
    page.title = "simple weekly calendar"
    page.bgcolor = style.WHITE
    page.padding = 0
    page.window.min_width = 800
    page.window.min_height = 600
    page.window.title_bar_hidden = True
    page.window.title_bar_buttons_hidden = True

    layout = ft.Column(
        expand=1,
        spacing=0,
        controls=[
            Title_bar(),
            ft.Row(
                expand=1,
                spacing=0,
                controls=[Day_box(i) for i in range(4)]
            ),
            ft.Row(
                expand=1,
                spacing=0,
                controls=[Day_box(i) for i in range(4, 8)]
            ),
        ]
    )

    page.add(layout)
    page.update()

ft.run(main)