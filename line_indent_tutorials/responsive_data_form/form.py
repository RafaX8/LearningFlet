import flet as ft
import form_data as fdata


class Form(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            border=ft.border.all(
                width=1,
                color=ft.colors.RED_50
            ),
            padding=20,
            border_radius=6
        )

        divider = ft.Divider(
            height=10,
            color='transparent'
        )

        self.title = ft.TextField(
            bgcolor='transparent'
        )
        self.tags = ft.Row(
            controls=self.render_tags(),
            wrap=True
        )

        self.name = ft.TextField(
            bgcolor='transparent',
            expand=1
        )
        self.link = ft.TextField(
            bgcolor='transparent',
            expand=2
        )

        media_row = ft.Row(
            controls=[
                self.name,
                self.link
            ]
        )

        self.commit = ft.TextButton(
            'Commit Line!',
            height=45,
        )

        commit_row = ft.Row(
            controls=[
                self.commit,
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        self.content = ft.Column(
            controls=[
                ft.Text(
                    value='Form content'
                ),
                self.title,
                divider,
                ft.Text(
                    value='Select Tags 🏷'
                ),
                self.tags,
                divider,
                ft.Text(
                    value='Add Media'
                ),
                media_row,
                divider,
                commit_row
            ],
            expand=True
        )

    def render_tags(self) -> list[ft.Container]:
        return [
            ft.Container(
                content=ft.Text(
                    value=render_tag_name,
                    size=11,
                    weight=ft.FontWeight.BOLD
                ),
                bgcolor=render_tag_bgcolor,
                padding=6,
                border_radius=4,
                animate=ft.Animation(
                    duration=1000,
                    curve=ft.animation.AnimationCurve.DECELERATE,
                ),
                on_click=lambda _, tag_name=render_tag_name, tag_bgcolor=render_tag_bgcolor, tag_remark_color=render_tag_remark_color:
                fdata.FormData.update_tags(
                    tag=[tag_name, tag_bgcolor, tag_remark_color],
                    form=self
                ),
            )
            for render_tag_name, render_tag_bgcolor, render_tag_remark_color in fdata.FormData.tags
        ]
