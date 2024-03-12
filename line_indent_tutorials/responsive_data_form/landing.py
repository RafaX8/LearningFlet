import flet as ft


class Landing(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            padding=ft.padding.only(
                top=0,
                left=20,
                right=20,
                bottom=15
            ),
            col={
                'sm': 12,
                'md': 12,
                'lg': 6
            },
            bgcolor='white10'
        )

        self.title = ft.Text(
            value='LineIndent Tutorials',
            size=30,
        )

        self.subtitle = ft.Text(
            value='Subtitle for LineIndent Tutorials',
            size=15
        )

        self.content = ft.Column(
            controls=[
                self.title,
                self.subtitle
            ],
            expand=True
        )
