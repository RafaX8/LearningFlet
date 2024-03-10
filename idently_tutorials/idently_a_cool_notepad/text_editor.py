import flet as ft


class TextEditor(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.text_field = ft.TextField(
            multiline=True,
            autofocus=True,
            border=ft.InputBorder.NONE,
            min_lines=40,
            on_change=self.save_text,
            content_padding=30,
            cursor_color='yellow'
        )

    def save_text(self, e: ft.ControlEvent) -> None:
        with open('idently_tutorials/idently_a_cool_notepad/text.txt', 'w') as f:
            f.write(self.text_field.value)

    def read_text(self) -> str | None:
        self.text_field.hint_text = 'Welcome to your notepad!'
        try:
            with open('idently_tutorials/idently_a_cool_notepad/text.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def build(self) -> ft.TextField:
        self.text_field.value = self.read_text()
        return self.text_field
