import flet as ft


def main(page: ft.Page) -> None:
    page.title = 'Keyboard shortcuts'
    page.spacing = 30
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    key: ft.Text = ft.Text(value='Key', size=30, color='purple')
    shift: ft.Text = ft.Text(value='Shift', size=30, color='green')
    ctrl: ft.Text = ft.Text(value='Ctrl', size=30, color='red')
    alt: ft.Text = ft.Text(value='Alt', size=30, color='orange')
    meta: ft.Text = ft.Text(value='Meta', size=30, color='blue')  # Windows key doesn't work (yet I suppose)

    keyboard: list[ft.Text] = [key, shift, ctrl, alt, meta]

    def on_key_pressed(e: ft.KeyboardEvent) -> None:
        key.value = e.key
        shift.visible = e.shift
        ctrl.visible = e.ctrl
        alt.visible = e.alt
        meta.visible = e.meta

        print(e.ctrl, e.key)

        match e.ctrl, e.key:
            case True, 'S':
                print('Ctrl + S pressed! -> SAVE')
                page.bgcolor = ft.colors.BLUE_50
            case True, 'C':
                print('Ctrl + C pressed! -> COPY')
                page.bgcolor = ft.colors.GREEN_50
            case True, 'V':
                print('Ctrl + V pressed! -> PASTE')
                page.bgcolor = ft.colors.RED_50
            case True, 'X':
                print('Ctrl + X pressed! -> CUT')
                page.bgcolor = ft.colors.ORANGE_50
            case True, 'Z':
                print('Ctrl + Z pressed! -> UNDO')
                page.bgcolor = ft.colors.PURPLE_50
            case True, 'Y':
                print('Ctrl + Y pressed! -> REDO')
                page.bgcolor = ft.colors.AMBER_50
            case _, _:
                print('Shortcut not found!')
                page.bgcolor = ft.colors.WHITE

        page.update()

    page.on_keyboard_event = on_key_pressed

    page.add(
        ft.Text('Press any combination of keys... # Windows key doesn\'t work (yet I suppose)'),
        ft.Row(
            controls=keyboard,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    ft.app(target=main)
