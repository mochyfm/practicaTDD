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

        self.assertEqual(test_funcionamiento.getValorInicial(), inicial)
        self.assertEqual(test_funcionamiento.getIncrementador(), incremento)
        self.assertEqual(test_funcionamiento.getLimite(), limite)

    def test_valores_default(self):

        """ Declaramos la variable que utilizaremos para realizar la comprobación """

        limite = 5

        """ Creamos el Constructor asignando únicamente el valor del límite """

        test_valores_default = Contador(limite=limite) 

        """ Verificamos que los valores que no han sido asignados tienen los valores esperados """

        self.assertEqual(test_valores_default.getValorInicial(), 0)
        self.assertEqual(test_valores_default.getIncrementador(), 1)

    def test_igualacion_valores(self):

        """ Declaramos las variables a las que queremos igualar el contador """

        inicial = 0
        incremento = 2
        limite = 5

        """ Creamos el Constructor asignando únicamente el valor del límite """

        test_igualacion_valores = Contador(inicial, incremento, limite)

        """ Igualamos los valores y comprobamos posteriormente si NO han sido igualados, 
            ya que se pide que no sea igual """

        self.assertNotEqual(test_igualacion_valores.getValorInicial(), 5)
        self.assertEqual(test_igualacion_valores.getValorInicial(), inicial)

        self.assertNotEqual(test_igualacion_valores.getIncrementador(), 1)
        self.assertEqual(test_igualacion_valores.getIncrementador(), incremento)
        
        self.assertNotEqual(test_igualacion_valores.getLimite(), 10)
        self.assertEqual(test_igualacion_valores.getLimite(), limite)
        
    if __name__ == '__main__':
        unittest.main()