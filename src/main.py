import flet as ft
from datetime import datetime


def main(page: ft.Page):
    # 색상 상수
    SAGE_GREEN = "#A5BB7A"
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
    page.padding = 0
    page.window.min_width = 800
    page.window.min_height = 600
    page.window.title_bar_hidden = True
    page.window.title_bar_buttons_hidden = True

    # date picker
    date_picker = ft.DatePicker(
        first_date=datetime(year=2026, month=1, day=1),
        last_date=datetime.now()
    )
    page.overlay.append(date_picker)
    page.update()

    # async function
    async def pick_files():
        await ft.FilePicker().pick_files()
    
    async def save_file():
        await ft.FilePicker().save_file()
    
    async def close_window():
        await page.window.close()

    # title bar
    def create_title_bar():
        # create icon btn
        def create_icon_btn(icon, tooltip=None, on_click=None):
            return ft.IconButton(
                icon=icon,
                icon_size=17,
                icon_color=WHITE,
                tooltip=tooltip,
                on_click=on_click,
                style=ft.ButtonStyle(
                    padding=10,
                    overlay_color=ft.Colors.with_opacity(0.1, WHITE),
                    shape=ft.RoundedRectangleBorder(radius=8),
                ),
            )

        # left: utility
        left_row = ft.Row(
            spacing=4,
            alignment=ft.MainAxisAlignment.START,
            controls=[
                create_icon_btn(
                    ft.Icons.UPLOAD_FILE,
                    "Load",
                    on_click=pick_files,
                ),
                create_icon_btn(
                    ft.Icons.SAVE,
                    "Save",
                    on_click=save_file,
                ),
                create_icon_btn(
                    ft.Icons.CALENDAR_MONTH,
                    "Pick date",
                    on_click=lambda _: setattr(date_picker, 'open', True),
                ),
            ],
        )

        # middle: title(dragable)
        middle_title = ft.WindowDragArea(
            expand=1,
            content=ft.Container(
                expand=1,
                alignment=ft.Alignment.CENTER,
                content=ft.Text(
                    "Simple Weekly Calendar",
                    size=15,
                    weight=ft.FontWeight.W_500,
                    color=WHITE,
                ),
            )
        )

        # right: window button
        right_row = ft.Row(
            spacing=4,
            alignment=ft.MainAxisAlignment.END,
            controls=[
                create_icon_btn(
                    ft.Icons.REMOVE,
                    "Minimize",
                    on_click=lambda _: setattr(page.window, 'minimized', True)
                ),
                create_icon_btn(
                    ft.Icons.CROP_SQUARE,
                    "Maximize",
                    on_click=lambda _: setattr(
                        page.window, 'maximized', not page.window.maximized)
                ),
                create_icon_btn(
                    ft.Icons.CLOSE,
                    "Close",
                    on_click=close_window
                )
            ]
        )

        return ft.Container(
            height=40,
            bgcolor=SAGE_GREEN,
            content=ft.Row(
                spacing=0,
                expand=1,
                controls=[
                    ft.Container(content=left_row),
                    middle_title,
                    ft.Container(content=right_row),
                ],
            ),
        )

    # day box
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
                    1, DIVIDER_COLOR) if index < 4 else None
            ),
        )

    layout = ft.Column(
        expand=1,
        spacing=0,
        controls=[
            create_title_bar(),
            ft.Row(
                expand=1,
                spacing=0,
                controls=[create_day_box(i) for i in range(4)]
            ),
            ft.Row(
                expand=1,
                spacing=0,
                controls=[create_day_box(i) for i in range(4, 8)]
            ),
        ]
    )

    page.add(layout)
    page.update()

ft.run(main)