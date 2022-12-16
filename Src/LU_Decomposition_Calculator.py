# --------------------- Imports ---------------------
import copy
import numpy as np


# --------------------- Separator ---------------------
class Step:
    def __init__(self, M: list[list], stepExplanation: str):
        self.__M = M
        self.__stepExplanation = stepExplanation

    def showStep(self):
        print(self.__stepExplanation)
        print(np.array(self.__M))


class Steps:
    def __init__(self):
        self.__steps = []
        self.__FLOPS = 0

    def incFlops(self, c):
        self.__FLOPS += c

    def addStep(self, s: Step):
        self.__steps.append(s)

    def showSteps(self):
        print(f"FLOPS = {self.__FLOPS}")
        for step in self.__steps:
            step.showStep()


class LUAnswer:
    def __init__(self, L: list[list], U: list[list], steps: Steps):
        self.__L = L
        self.__U = U
        self.__steps = steps

    def showAns(self):
        # print("Matrix L:")
        # print(np.array(self.__L))
        # print("Matrix U:")
        # print(np.array(self.__U))
        self.__steps.showSteps()


# --------------------- Separator ---------------------
def crout(A: list[list]):
    L = []
    U = []
    problemSteps = Steps()
    for i in range(len(A)):
        L.append([])
        U.append([])
        for j in range(len(A)):
            L[-1].append(0)
            U[-1].append(0)
            if j == i:
                U[i][j] = 1
    problemSteps.addStep(Step(copy.deepcopy(L), "L Matrix"))
    problemSteps.addStep(Step(copy.deepcopy(U), "U Matrix"))
    for j in range(len(A)):
        # Lower Matrix Element Calculation      - Consider the j as iterating over each column
        for i in range(j, len(A)):                  # iterating over each element in the column of the lower matrix.
            s = 0
            for k in range(j):                      # up to j, so we can stop iterating at the diagonal element.
                s += L[i][k] * U[k][j]
                problemSteps.incFlops(2)            # addition and multiplication
            L[i][j] = A[i][j] - s
            problemSteps.incFlops(1)                # subtraction
            problemSteps.addStep(Step(copy.deepcopy(L), f"L Matrix >> L[{i}][{j}] = A[{i}][{j}] - {s}"))
        # Upper Matrix Element Calculation      - Consider the j as iterating over each row
        for i in range(j, len(A)):
            s = 0
            for k in range(j):
                s += L[j][k] * U[k][i]
                problemSteps.incFlops(2)            # addition and multiplication
            if L[j][j] == 0:
                print(f"L[{j}][{j}] == 0")
                exit(101)
            U[j][i] = (A[j][i] - s) / L[j][j]
            problemSteps.incFlops(2)                # subtraction and division
            problemSteps.addStep(Step(copy.deepcopy(U), f"U Matrix >> U[{j}][{i}] = (A[{j}][{i}] - {s}) / L[{j}][{j}]"))
    return LUAnswer(L, U, problemSteps)
