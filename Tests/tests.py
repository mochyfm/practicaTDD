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

    def test_valores_default(self):

        """ Declaramos la variable que utilizaremos para realizar la comprobación """

        limite = 5

        """ Creamos el Constructor asignando únicamente el valor del límite """

        test_valores_default = Contador(limite=limite) 

        """ Verificamos que los valores que no han sido asignados tienen los valores esperados """

        self.assertEqual(test_valores_default.valor_inicial, 0)
        self.assertEqual(test_valores_default.incremento, 1)    