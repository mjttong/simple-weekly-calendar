import flet as ft
from datetime import datetime


def main(page: ft.Page):
    # 색상 상수
    SAGE_GREEN = ft.Colors.GREEN_300
    TEXT_COLOR = ft.Colors.GREY_800
    DATE_COLOR = ft.Colors.GREY_700
    DIVIDER_COLOR = ft.Colors.GREY_200
    WHITE = ft.Colors.WHITE

    # 요일
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Memo"]
    today_idx = datetime.now().weekday()

    # page default settings
    page.title = "simple weekly calendar"
    page.bgcolor = WHITE
    page.padding = 15
    page.window.min_width = 800
    page.window.min_height = 600

    def create_day_box(index: int):
        title_text = days[index]
        is_today = index == today_idx

        # 오늘인 경우 강조
        title_color = SAGE_GREEN if is_today else DATE_COLOR
        title_weight = ft.FontWeight.BOLD if is_today else ft.FontWeight.W_500

        # content
        container_title = ft.Text(
            value=title_text,
            color=title_color,
            weight=title_weight,
            size=20,
        )
        container_text = ft.TextField(
            expand=1,
            multiline=True,
            min_lines=2,
            border=ft.InputBorder.NONE,
            text_size=14,
            color=TEXT_COLOR,
            cursor_color=SAGE_GREEN,
            hint_text="Write here...",
            hint_style=ft.TextStyle(color=ft.Colors.GREY_300),
        )

        return ft.Container(
            expand=1,
            padding=25,
            content=ft.Column(
                spacing=10,
                controls=[container_title, container_text],
            ),
            border=ft.Border.only(
                right=ft.BorderSide(1, DIVIDER_COLOR) if (
                    index + 1) % 4 != 0 else None,
                bottom=ft.BorderSide(
                    1, DIVIDER_COLOR) if index < 4 else None  # 윗줄은 바닥 선 추가
            ),
        )

    layout = ft.Column(
        expand=1,
        spacing=0,
        controls=[
            ft.Row(expand=1, spacing=0, controls=[
                   create_day_box(i) for i in range(4)]),
            ft.Row(expand=1, spacing=0, controls=[
                   create_day_box(i) for i in range(4, 8)]),
        ]
    )

    page.add(layout)
    page.update()

ft.run(main)