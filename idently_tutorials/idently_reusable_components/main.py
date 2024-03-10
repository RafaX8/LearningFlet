import flet as ft
import reusable_component as rc


class IncrementCounter(ft.UserControl):
    def __init__(self, text: str, start_number: int = 0) -> None:
        super().__init__()
        self.text: str = text
        self.counter: int = start_number
        self.text_number: ft.Text = ft.Text(
            value=str(self.counter),
            size=40
        )

    def increment(self, e: ft.ControlEvent) -> None:
        self.counter += 1
        self.text_number.value = str(self.counter)
        self.update()

    def build(self) -> ft.Row:
        return ft.Row(
            controls=[
                ft.ElevatedButton(
                    text=self.text,
                    on_click=self.increment,
                ),
                self.text_number
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            width=500
        )


def main(page: ft.Page) -> None:
    page.title = 'Reusable components'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.update()

    for x in range(2):
        page.add(
            IncrementCounter(
                text=f'Reusable inside for loop {x + 1}',
                start_number=x
            )
        )

    page.add(IncrementCounter(text='Reusable outside for loop', start_number=15))
    page.add(rc.DecrementCounter(text='Reusable imported from another file', start_number=15))

    page.update()


if __name__ == '__main__':
    ft.app(target=main)
