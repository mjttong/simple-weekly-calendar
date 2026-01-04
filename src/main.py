import flet as ft

def main(page: ft.Page):
    # page default settings
    page.title = "simple weekly calendar"

    def create_container() -> list[ft.Control]:
        return [ft.Container(
            bgcolor=ft.Colors.AMBER,
            expand=1,
            content=ft.TextField()
        ) for _ in range(4)]
    
    # column
    col = ft.Column(
        expand=1,
        controls=[
            ft.Row(controls=create_container(), expand=1),
            ft.Row(controls=create_container(), expand=1)
        ]
    )

    page.add(col)
    page.update()


ft.run(main)