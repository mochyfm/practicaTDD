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

    def test_incrementar(self):
        
        """ Declaramos el contador que vamos a utilizar para el test """

        inicial = 0
        incremento = 5
        limite = 20

        test_incrementar = Contador(inicial, incremento, limite)

        """ Utilizamos la funcion Incrementar para que incremente una vez el valor del contador, 
            y lo almacenamos en una variable """

        resultado = test_incrementar.Incrementar()

        """ Comprobamos que el valor es el resultado del valor inicial más el incrementador, 
        ya que deberá haberse incrementado una vez. Pondremos evidentemente que si el límite es igual 
        o menor que al incrementador, deberá ser el valor inicial ya que es lo que se nos pide """

        if incremento >= limite:
            self.assertEqual(test_incrementar.getIncrementador(), inicial)
        else: 
            self.assertEqual(resultado, inicial + incremento)

        # También comprobamos que el valor se almacena correctamente tanto en el Getter del incrementador 
        # como en el propio resultado de este.

        self.assertEqual(test_incrementar.getIncrementador(), resultado) 

    def test_reset(self):

        """ Declaramos el contador que vamos a utilizar para el test """

        inicial = 0
        incremento = 10
        limite = 50

        test_reset = Contador(inicial, incremento, limite)

        """ Utilizamos la funcion Incrementar para que incremente varias veces el valor del contador """

        test_reset.Incrementar()
        test_reset.Incrementar()
        test_reset.Incrementar()

        """ Una vez tenemos un valor decente, reseteamos el contador """

        test_reset.reset()

        """ Y ahora comprobamos que se ha reseteado correctamente """

        self.assertEqual(test_reset.getValorActual(), inicial) 
        self.assertEqual(test_reset.getValorActual(), test_reset.getValorInicial()) 

    if __name__ == '__main__':
        unittest.main()