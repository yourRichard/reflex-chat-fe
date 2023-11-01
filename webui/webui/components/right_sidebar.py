import reflex as rx



def right_sidebar():
    return rx.box(
        rx.flex(
        # add icon
rx.avatar(
        rx.avatar_badge(
            box_size="1rem",
            bg="green.200",
            border_color="black",
        ),
        name="Barack Obama",
    ),        rx.button(
            "Share",
             px="4",
             color="black",
             py="2px",
             h="auto",
             border_radius="10px"
        )
    )
    )
    

