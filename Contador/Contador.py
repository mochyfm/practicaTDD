class Contador:

    def __init__(self, valor_inicial=0, incremento=1, limite=None):
        self.__valor_inicial = valor_inicial
        self.__incremento = incremento
        self.__limite = limite
        self.__valor_actual = valor_inicial

    def getValorInicial(self):
        return self.__valor_inicial

    def getValorActual(self):
        return self.__valor_actual

    def getIncrementador(self):
        return self.__incremento

    def getLimite(self):
        return self.__limite

    def Incrementar(self):
        return self.__valor_actual + self.__incremento