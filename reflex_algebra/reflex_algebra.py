import reflex as rx
import ast
from reflex_algebra.componentes.m_view import matrices_v, MatrizState
from reflex_algebra.componentes.alert import alert_nm

def index():
    return rx.box(
        rx.container(
            rx.center(
                rx.text("Multiplicación de Matrices", font_size="3em"),
            )
        ),
        rx.grid(
            rx.container(
                rx.center(rx.text("Ingrese la primer matriz:")),
                rx.flex(
                    rx.input(placeholder="Ingrese la matriz A", on_change=MatrizState.set_textA, value=MatrizState.textA),
                    rx.button("Obtener Matriz A",on_click=MatrizState.convertir),
                    width="100%",
                    justify="center",
                    spacing="2"
                ),
                matrices_v(MatrizState.S_A,MatrizState.ncA,MatrizState.nrA),
                spacing="2",
            ),
            rx.container(
                rx.flex(
                    rx.button("Limpiar", on_click=MatrizState.Clear),
                    width="100%",
                    heigth="100%",
                    align="center",
                    justify="center",
                    spacing="2"
                )
            ),
            rx.container(
                rx.center(rx.text("Ingrese la segunda matriz:")),
                rx.flex(
                    rx.input(placeholder="Ingrese la matriz B",on_change=MatrizState.set_textB, value=MatrizState.textB),
                    rx.button("Obtener Matriz B", on_click=MatrizState.convertirB),
                    width="100%",
                    justify="center",
                    spacing="2"
                ),
                matrices_v(MatrizState.S_B,MatrizState.ncB,MatrizState.nrB),
                spacing="2",
            ),
            columns="3",
            spacing="4",
            width="100%",
            padding="0 1em"
        ),
        rx.flex(
            rx.center(
                rx.button("Multiplicar matricez A x B", on_click = MatrizState.Get_AB),
            ),
            rx.container(
                rx.cond(
                    MatrizState.Multiplicable,
                    matrices_v(MatrizState.S_AB, MatrizState.cAB,MatrizState.rAB),
                    alert_nm()
                )
            ),
            spacing="2",
            direction="column",
            margin="2em 0",
        )
    )

app=rx.App(
    theme=rx.theme(
        appearance="dark"
    )
)
app.add_page(index, route="/")
