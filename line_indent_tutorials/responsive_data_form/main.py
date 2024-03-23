import flet as ft
import landing
import form


def get_divider() -> ft.Divider:
    return ft.Divider(
        height=10,
        color='transparent'
    )


def get_form_container() -> ft.Container:
    return ft.Container(
        form.Form(),
        padding=ft.padding.only(
            left=20,
            right=20
        ),
        col={
            'sm': 12,
            'md': 12,
            'lg': 6
        }
    )


def get_responsive_row() -> ft.ResponsiveRow:
    return ft.ResponsiveRow(
        controls=[
            landing.Landing(),
            get_form_container()
        ],
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )


def get_container() -> ft.Container:
    border = ft.BorderSide(
        width=2,
        color='white10'
    )
    return ft.Container(
        content=get_responsive_row(),
        border=ft.border.only(
            top=border,
            bottom=border
        ),
        padding=ft.padding.only(
            top=20,
            bottom=20
        ),
        alignment=ft.alignment.center
    )


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.BLUE
    )
    page.scroll = ft.ScrollMode.AUTO
    page.add(
        ft.SafeArea(
            ft.Stack(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            [
                                get_divider(),
                                get_container()
                            ]
                        )
                    )
                ],
                expand=True,
            )
        )
    )


if __name__ == '__main__':
    ft.app(target=main)
