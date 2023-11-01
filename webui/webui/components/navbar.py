import reflex as rx

from webui import styles
from webui.state import State


def navbar():
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.icon(
                    tag="hamburger",
                    mr=4,
                    on_click=State.toggle_drawer,
                    cursor="pointer",
                ),
                rx.link(
                    rx.box(
                        rx.image(src="logo-dark.svg",width=60,height=50),
                    ),
                    href="/",
                ),
                
            ),
            rx.hstack(
                rx.button(
                    "+ New chat",
                    bg=styles.accent_color,
                    px="4",
                    py="2",
                    h="auto",
                    on_click=State.toggle_modal,
                ),
                rx.menu(
                    rx.menu_button(
                        rx.avatar(name="User", size="md"),
                        rx.box(),
                    ),
                    rx.menu_list(
                        rx.menu_item("Help"),
                        rx.menu_divider(),
                        rx.menu_item("Settings"),
                    ),
                ),
                spacing="8",
            ),
            justify="space-between",
        ),
        bg=styles.bg_dark_color,
        backdrop_filter="auto",
        backdrop_blur="lg",
        p="4",
        position="sticky",
        top="0",
        z_index="100",
    )
