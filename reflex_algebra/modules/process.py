import numpy as np

#A = [[1,2,-3],[4,0,-2]]
#B = [[3,1],[2,4],[-1,5]]

# A = [[1,-1,2],[3,2,4],[4,-2,3]]
# B = [[1,0,-1],[3,3,-3],[4,2,5]]

#A = [[2,3,1],[3,-4,5],[1,-1,-2]]
#B = [[1,0,-3],[-2,1,5],[3,4,2]]


#A = [[2,-3,4],[-1,2,3],[5,-1,-2]]
#B = [[2],[1],[4]]

#rA, cA = np.array(A).shape
#rB, cB = np.array(B).shape

# AB = rA x cB
def AB(A, B, rA, rB, cA, cB):
    AB = []
    CaJ = 0

    if rB == cA:
        while np.array(AB).shape != (rA, cB):
            ABc = []
            CbI = 0
            for fila in range(cB):
                resultado = 0
                for i in range(rB):
                    Bi = B[i][CbI]
                    Aj = A[CaJ][i]
                    resultado += Aj * Bi
                print(resultado)
                ABc.append(resultado)
                print(ABc)
                if cB != 1:
                    CbI += 1

            AB.append(ABc)
            CaJ += 1
        print(f"El resultado es {AB}")
        return AB
    else:
        return False
