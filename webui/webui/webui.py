"""The main Chat app."""

import reflex as rx

from webui import styles
from webui.components import chat, modal, navbar, sidebar,right_sidebar,main_middle
from webui.state import State


def index() -> rx.Component:
    """The main app."""
    return rx.vstack(
        rx.grid(
            rx.grid_item(
                right_sidebar(),
                row_span=1,
                col_span=2 ,
                bg='white',
                h="100%",
                margin_top="20px",
                width="80%"
            ),
            rx.grid_item(
                main_middle(),
                row_span=2,
                col_span=5,
                h="90%",
                width="74%",
                margin_top="20px",
                magin_right="10px",
                position="absolute",
                margin_left="20.5rem"

            ),
                template_rows="repeat(2, 1fr)",
                template_columns="repeat(7, 1fr)",
        ),
        bg=styles.bg_dark_color,
        color=styles.text_light_color,
        min_h="100vh",
        align_items="stretch",
        spacing="0",
        justify_contect="space-between"
    )


# Add state and page to the app.
app = rx.App(state=State, style=styles.base_style)
app.add_page(index)
app.compile()
