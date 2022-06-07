class Contador:

    def __init__(self, valor_inicial=0, incremento=1, limite=None):
        self.valor_inicial = valor_inicial
        self.incremento = incremento
        self.limite = limite
        self.valor_actual = valor_inicial
