import copy
import math

class term:
    def __init__(self, type, spec, coeff):
        self.type = type
        self.spec = spec
        self.coeff = coeff

    def set_type(self, type): self.type = type
    def get_type(self): return self.type

    def set_spec(self, spec): self.spec = spec
    def get_spec(self): return self.spec

    def set_coeff(self, coeff): self.coeff = coeff
    def get_coeff(self): return self.coeff

    def eval(self, x):
        y = 0
        match type:
            case 'poly':
                y = x**self.spec
            case 'exp':
                y = self.spec**x
            case 'sin':
                y = math.sin(self.spec*x)
            case 'cos':
                y = math.cos(self.spec*x)
        return self.coeff * y

    def derivative(self):
        match type:
            case 'poly':
                if self.get_spec == 0:
                    return None
                else:
                    return term('poly', self.spec-1 , self.coeff*self.spec)
            case 'exp':
                return term('exp' , self.spec , self.coeff*math.log(self.spec))
            case 'sin':
                return term('cos' , self.spec , self.coeff*self.spec)
            case 'cos':
                return term('sin' , self.spec , -1*self.coeff*self.spec)

class Function:

    def __init__(self, expr: list[term]):
        self.__expression = copy.deepcopy(expr)

    def f_eval(self, x):
        y = 0
        for t in self.__expression:
            if t is None: continue
            y += t.eval(x)
        return y

    def f_derivative(self):
        fdash = []
        for t in self.__expression:
            if t is None: continue
            fdash.append(t.derivative())
        return Function(fdash)
