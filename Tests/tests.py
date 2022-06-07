import unittest
from Contador.Contador import Contador

class TestContador(unittest.TestCase):
    
    """ Test para comprobar los resultados del contador """
    
    def test_creacion_contador(self):

        """ Declaramos las variables que asignaremos en el constructor y usaremos para la comprobación
            de los assert """

        inicial = 0
        incremento = 2
        limite = 5


        """ Asignamos valores en todos los campos """

        test_funcionamiento = Contador(inicial, incremento, limite)


        """ Verifica que los valores se asignan como deberian """

        self.assertEqual(test_funcionamiento.valor_inicial, inicial)
        self.assertEqual(test_funcionamiento.incremento, incremento)
        self.assertEqual(test_funcionamiento.limite, limite)