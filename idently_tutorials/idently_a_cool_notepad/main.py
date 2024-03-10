import flet as ft
import text_editor as te


def main(page: ft.Page):
    page.title = "A cool Notepad __init__?"
    page.add(te.TextEditor())


if __name__ == "__main__":
    ft.app(target=main)
