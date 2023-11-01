import reflex as rx
from webui import styles
from webui.components import loading_icon
from webui.state import QA, State

def main_middle():
    return rx.box(
        rx.flex(

            rx.box(
            rx.text(
            "Unlock the power of AI",
            font_size="1.8rem",
            as_="b",
            margin_left="190px",
            color="#FEFEFE"
            
        ),
        rx.text(
            "Chat with the smartest AI - Experience the power of AI with us",
            font_size="1.4rem",
            color="#607275",
            margin_left="40px",

        ),

rx.flex(
    rx.icon(
        tag="edit",
        font_size="3.6rem",
        bg="#382F4E",
        color="#8E55EA",
        px="4",
        py="4",
        border_radius="10px"
    ),
    rx.text(
        "Photo editing",
        as_="b",
        font_size="1.2rem",
        text_align="center",
        color="#FEFEFE",
        margin_left="30px",
        margin_top="12px",
    ),
    rx.icon(
        tag="arrow_forward",
        color="#6C7275",
        font_size="2rem",
        margin_left="235px",
        margin_top="12px"
    ),
    padding="10px",
    border_radius="10px",
    cursor="pointer",
    transition="0.4s",
    border="1px solid #343839",
    width="70%",

    _hover= {
        "bg": "#141718",

    }, 
    margin_left="95px",
    margin_top="45px",
),
rx.flex(
    rx.icon(
        tag="chevron_right",
        font_size="3.6rem",
        bg="#472D22",
        color="#D84C10",
        px="4",
        py="4",
        border_radius="10px"
    ),
    rx.text(
        "Video generation",
        as_="b",
        font_size="1.2rem",
        text_align="center",
        color="#FEFEFE",
        margin_left="30px",
        margin_top="12px",
    ),
    rx.icon(
        tag="arrow_forward",
        color="#6C7275",
        font_size="2rem",
        margin_left="201px",
        margin_top="12px"
    ),
    padding="10px",
    border_radius="10px",
    cursor="pointer",
    transition="0.4s",
    border="1px solid #343839",
    width="70%",

    _hover= {
        "bg": "#141718",
    }, 
    margin_left="95px",
    margin_top="23px",
),
rx.flex(
    rx.icon(
        tag="star",
        font_size="3.6rem",
        bg="#1C3852",
        color="#0084FF",
        px="4",
        py="4",
        border_radius="10px"
    ),
    rx.text(
        "Education feedback",
        as_="b",
        font_size="1.2rem",
        text_align="center",
        color="#FEFEFE",
        margin_left="30px",
        margin_top="12px",
    ),
    rx.icon(
        tag="arrow_forward",
        color="#6C7275",
        font_size="2rem",
        margin_left="181px",
        margin_top="12px"
    ),
    padding="10px",
    border_radius="10px",
    cursor="pointer",
    transition="0.4s",
    border="1px solid #343839",
    width="70%",

    _hover= {
        "bg": "#141718",

    }, 
    margin_left="95px",
    margin_top="23px",
),
rx.flex(
    rx.icon(
        tag="drag_handle",
        font_size="3.6rem",
        bg="#2C4334",
        color="#52BA69",
        px="4",
        py="4",
        border_radius="10px"
    ),
    rx.text(
        "code generation",
        as_="b",
        font_size="1.2rem",
        text_align="center",
        color="#FEFEFE",
        margin_left="30px",
        margin_top="12px",
    ),
    rx.icon(
        tag="arrow_forward",
        color="#6C7275",
        font_size="2rem",
        margin_left="210px",
        margin_top="12px"
    ),
    padding="10px",
    border_radius="10px",
    cursor="pointer",
    transition="0.4s",
    border="1px solid #343839",
    width="70%",

    _hover= {
        "bg": "#141718",

    }, 
    margin_left="95px",
    margin_top="23px",
),
rx.flex(
    rx.icon(
        tag="link",
        font_size="3.6rem",
        bg="#4A3A25",
        color="#E68A1D",
        px="4",
        py="4",
        border_radius="10px"
    ),
    rx.text(
        "Audio generation",
        as_="b",
        font_size="1.2rem",
        text_align="center",
        color="#FEFEFE",
        margin_left="30px",
        margin_top="12px",
    ),
    rx.icon(
        tag="arrow_forward",
        color="#6C7275",
        font_size="2rem",
        margin_left="201px",
        margin_top="12px"
    ),
    padding="10px",
    border_radius="10px",
    cursor="pointer",
    transition="background 0.6s",
    border="1px solid #343839",
    width="70%",
    

    _hover= {
        "bg": "#141718",
    }, 
    margin_left="95px",
    margin_top="23px",
),

    overflow="auto",
    width="73%",
    h="100%"
    ),

    rx.box(
       rx.text(
            "This is a text"
              )
        ),
        bg="#232627",
        padding_top="35px",
        h="78%",
        overflow="hidden"
        ),
        rx.box(
        rx.flex(
            rx.icon(

                tag="add", 
                color="#35393B", 
                font_size="1.5rem", 
                position="absolute",
                margin_left="30px",
                margin_top="50px",
                z_index="1000",
                bg="#6C7275",
                px="1.5",
                py="1.5",
                border_radius="50%",
                cursor="pointer",
                transition="0.5s",
                _hover={
                    "bg":"#0084FF"
                },
            ),
            rx.input(
             
                placeholder="Ask OpenAgent anything",
                value=State.question,
                on_change=State.set_question,
                _placeholder={"color": "#fffa"},
                hover={"border_color": styles.accent_color},
                style=styles.input_style,
                width="63%",
                padding_left="50px",
                padding="30px",
                margin_left="20px",
                margin_top="30px",
                border_radius="15px",
                border="2px solid #343839"

                ),
            rx.icon(

                tag="arrow_right", 
                color="#6C7275", 
                font_size="1.5rem", 
                position="absolute",
                margin_left="615px",
                margin_top="50px",
                z_index="1000",
                border_radius="50%",
                cursor="pointer",
                transition="0.5s",
                _hover={
                    "color":"#0084FF"
                },
            ),
        ),
    ),
            h="100%",
            overflow="hidden",
            bg="#232627",
            border_radius="20px",
            margin_top="15px"
)
           