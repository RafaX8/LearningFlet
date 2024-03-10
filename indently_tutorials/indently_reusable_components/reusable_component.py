import flet as ft


class DecrementCounter(ft.UserControl):
    def __init__(self, text: str, start_number: int = 0) -> None:
        super().__init__()
        self.text: str = text
        self.counter: int = start_number
        self.text_number: ft.Text = ft.Text(
            value=str(self.counter),
            size=40
        )

    def decrement(self, e: ft.ControlEvent) -> None:
        self.counter -= 1
        self.text_number.value = str(self.counter)
        self.update()

    def build(self) -> ft.Row:
        return ft.Row(
            controls=[
                ft.ElevatedButton(
                    text=self.text,
                    on_click=self.decrement,
                ),
                self.text_number
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            width=500
        )
