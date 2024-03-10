import flet as ft


def main(page: ft.Page) -> None:
    page.title = 'Increment counter'
    page.window_height = 200
    page.window_width = 500
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    text_number: ft.TextField = ft.TextField(
        value='0',
        text_align=ft.TextAlign.CENTER
    )

    def increment(e: ft.ControlEvent) -> None:
        text_number.value = str(int(text_number.value) + 1)
        page.update()

    def decrement(e: ft.ControlEvent) -> None:
        text_number.value = str(int(text_number.value) - 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=decrement),
                text_number,
                ft.IconButton(ft.icons.ADD, on_click=increment)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

    )


if __name__ == '__main__':
    ft.app(target=main)
