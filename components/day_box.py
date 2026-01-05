import flet as ft
import style
from datetime import datetime


class Day_box(ft.Container):
    def __init__(self, index):
        super().__init__()
        self.index = index
        self.expand = 1
        self.padding = 25
        self.content = ft.Column(
            spacing=10,
            controls=[self._create_container_title(), self._create_container_text()],
        )
        self.border = ft.Border.only(
            right=ft.BorderSide(1, style.DIVIDER_COLOR) if (
                index + 1) % 4 != 0 else None,
            bottom=ft.BorderSide(
                1, style.DIVIDER_COLOR) if index < 4 else None
        )

    def _create_container_title(self):
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Memo"]
        today_idx = datetime.now().weekday()

        title_text = days[self.index]
        is_today = self.index == today_idx

        # 오늘인 경우 강조
        title_color = style.SAGE_GREEN if is_today else style.DATE_COLOR
        title_weight = ft.FontWeight.BOLD if is_today else ft.FontWeight.W_500

        return ft.Text(
            value=title_text,
            color=title_color,
            weight=title_weight,
            size=20,
        )

    def _create_container_text(self):
        return ft.TextField(
            expand=1,
            multiline=True,
            min_lines=2,
            border=ft.InputBorder.NONE,
            text_size=14,
            color=style.TEXT_COLOR,
            cursor_color=style.SAGE_GREEN,
            hint_text="Write here...",
            hint_style=ft.TextStyle(color=ft.Colors.GREY_300),
        )
