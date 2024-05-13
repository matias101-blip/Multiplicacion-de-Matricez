import reflex as rx

def alert_nm ():
    return rx.callout.root(
        rx.callout.icon(rx.icon(tag="triangle_alert")),
        rx.callout.text("Estas matricez no se pueden multiplicar"),
        color_scheme="red",
        role="alert",
    )
