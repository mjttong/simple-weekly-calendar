import flet as ft
from datetime import datetime
import style


class Title_bar(ft.Container):
    def __init__(self):
        super().__init__()
        self.height = 40
        self.bgcolor = style.SAGE_GREEN
        self.content = ft.Row(
            spacing=0,
            expand=1,
            controls=[
                self._create_left_row(),
                self._create_middle_title(),
                self._create_right_row(),
            ],
        )
        self.date_picker = ft.DatePicker(
        first_date=datetime(year=2026, month=1, day=1),
        last_date=datetime.now()
    )

    # async function
    async def pick_files(self):
        await ft.FilePicker().pick_files()

    async def save_file(self):
        await ft.FilePicker().save_file()

    async def close_window(self):
        await self.page.window.close()  # type: ignore

    # date picker
    def did_mount(self):
        self.page.overlay.append(self.date_picker)
        self.page.update()

    def create_icon_btn(self, icon, tooltip=None, on_click=None):
        return ft.IconButton(
            icon=icon,
            icon_size=17,
            icon_color=style.WHITE,
            tooltip=tooltip,
            on_click=on_click,
            style=ft.ButtonStyle(
                padding=10,
                overlay_color=ft.Colors.with_opacity(0.1, style.WHITE),
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
        )

    # left: utility
    def _create_left_row(self):
        return ft.Container(ft.Row(
            spacing=4,
            alignment=ft.MainAxisAlignment.START,
            controls=[
                self.create_icon_btn(
                    ft.Icons.UPLOAD_FILE,
                    "Load",
                    on_click=self.pick_files,
                ),
                self.create_icon_btn(
                    ft.Icons.SAVE,
                    "Save",
                    on_click=self.save_file,
                ),
                self.create_icon_btn(
                    ft.Icons.CALENDAR_MONTH,
                    "Pick date",
                    on_click=lambda _: setattr(
                        self.date_picker, 'open', True),
                ),
            ],
        ))

    # middle: title(dragable)
    def _create_middle_title(self):
        return ft.WindowDragArea(
            expand=1,
            content=ft.Container(
                expand=1,
                alignment=ft.Alignment.CENTER,
                content=ft.Text(
                    "Simple Weekly Calendar",
                    size=15,
                    weight=ft.FontWeight.W_500,
                    color=style.WHITE,
                ),
            )
        )

    # right: window button
    def _create_right_row(self):
        return ft.Container(ft.Row(
            spacing=4,
            alignment=ft.MainAxisAlignment.END,
            controls=[
                self.create_icon_btn(
                    ft.Icons.REMOVE,
                    "Minimize",
                    on_click=lambda _: setattr(self.page.window, 'minimized', True)), # type: ignore
                self.create_icon_btn(
                    ft.Icons.CROP_SQUARE,
                    "Maximize",
                    on_click=lambda _: setattr(self.page.window, 'maximized', not self.page.window.maximized) # type: ignore
                ),
                self.create_icon_btn(
                    ft.Icons.CLOSE,
                    "Close",
                    on_click=self.close_window
                )
            ]
        ))
