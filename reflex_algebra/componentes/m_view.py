import reflex as rx
import numpy as np
import ast

from ..modules.process import AB
from ..componentes.alert import alert_nm

class MatrizState(rx.State):
    textA = ""
    textB = ""
    A = []
    A1 = []
    S_A = []
    B = []
    S_B = []
    ncA = 0
    nrA = 0
    ncB = 0
    nrB = 0
    AB = []
    rAB = 0
    cAB = 0
    S_AB = []
    Multiplicable = True

    def convertir(self):
        self.A= ast.literal_eval(self.textA)
        self.nrA, self.ncA = np.array(self.A).shape
        self.S_A = [item for sublist in self.A for item in sublist]

    def convertirB(self):
        self.B= ast.literal_eval(self.textB)
        self.nrB, self.ncB = np.array(self.B).shape
        self.S_B = [item for sublist in self.B for item in sublist]

    def Clear(self):
        self.A = []
        self.S_A = []
        self.textA = ""
        self.textB = ""
        self.B = []
        self.S_B = []
        self.AB = []
        self.S_AB = []
        self.Multiplicable = True

    def Get_AB(self):
        self.AB = AB(
            self.A,
            self.B,
            self.nrA,
            self.nrB,
            self.ncA,
            self.ncB
        )

        if self.AB == False:
            self.Multiplicable = False
        else:
            self.rAB, self.cAB = np.array(self.AB).shape
            self.S_AB = [item for sublist in self.AB for item in sublist]


def Cards(nombres: str):
    return rx.card(nombres)

def matrices_v(lista,nc,nr):
    return rx.grid(
        rx.foreach(lista, Cards),
        columns=f'{nc}',
        rows=f'{nr}',
        spacing="2",
    )
