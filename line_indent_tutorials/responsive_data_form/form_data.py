import flet as ft


class FormData:
    tags: list[list[str]] = [
        ['Programming', 'white10', ft.colors.ORANGE],
        ['Engineering', 'white10', ft.colors.AMBER],
        ['Software', 'white10', ft.colors.YELLOW],
        ['DataScience', 'white10', ft.colors.RED],
        ['Robotics', 'white10', ft.colors.GREEN],
        ['MachineLearning', 'white10', ft.colors.LIME],
        ['AI', 'white10', ft.colors.BLUE_GREY],
        ['WebDev', 'white10', ft.colors.BROWN],
        ['Electronics', 'white10', ft.colors.DEEP_ORANGE],
        ['Cybersecurity', 'white10', ft.colors.TEAL],
        ['Mathematics', 'white10', ft.colors.PINK],
        ['Physics', 'white10', ft.colors.PURPLE],
        ['Biotechnology', 'white10', ft.colors.INDIGO],
        ['ComputerVision', 'white10', ft.colors.LIGHT_GREEN],
        ['IoT', 'white10', ft.colors.LIGHT_BLUE_ACCENT],
        ['Database', 'white10', ft.colors.PURPLE_ACCENT],
    ]

    @staticmethod
    def update_tags(tag: list[str], form: object) -> None:  # to avoid circular imports, not a Form, but an object
        new_tag = [
            tag[0],
            ft.colors.with_opacity(
                opacity=0.5,
                color=tag[2]
            ),
            tag[2]
        ]

        FormData.tags = [
            new_tag if item[0] == new_tag[0] else [item[0], 'white10', item[2]]
            for item in FormData.tags
        ]

        form.tags.controls = form.render_tags()
        form.tags.update()
