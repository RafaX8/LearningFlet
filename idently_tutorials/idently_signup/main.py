import flet as ft
import hashlib


def main(page: ft.Page) -> None:
    page.title = 'Signup'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_height = 600
    page.window_width = 500
    page.window_resizable = False

    text_username: ft.TextField = ft.TextField(
        label='Username',
        text_align=ft.TextAlign.LEFT,
        width=200
    )
    text_password: ft.TextField = ft.TextField(
        label='Password',
        password=True,
        can_reveal_password=True,
        text_align=ft.TextAlign.LEFT,
        width=200
    )
    checkbox_signup: ft.Checkbox = ft.Checkbox(
        label='I agree to the stuff',
        value=False
    )
    button_submit: ft.ElevatedButton = ft.ElevatedButton(
        text='Sign Up 😊',
        width=200,
        disabled=True
    )

    def validate(e: ft.ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True

        page.update()

    def submit(e: ft.ControlEvent) -> None:
        hashed_password = hashlib.sha256(text_password.value.encode()).hexdigest()

        print(f'{text_username.label}: {text_username.value}')
        print(f'{text_password.label}: {hashed_password}')
        print(f'{checkbox_signup.label}: {checkbox_signup.value}')

        page.clean()
        page.add(
            ft.Row(
                controls=[
                    ft.Text(value=f'Welcome {text_username.value} 😊', size=20),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    text_username.on_change = validate
    text_password.on_change = validate
    checkbox_signup.on_change = validate
    button_submit.on_click = submit

    page.add(
        ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        text_username,
                        text_password,
                        checkbox_signup,
                        button_submit
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    )


if __name__ == '__main__':
    ft.app(target=main)
