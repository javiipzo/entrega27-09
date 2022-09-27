import unittest
from Calculator import Calculator
# Creamos una clase heredando de TestCase
class TestMyCalculator(unittest.TestCase):
 # Creamos una prueba para probar un valor inicial
    def setUp(self):
        self.calc = Calculator()
    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)
    # Creamos un nuevo test para comprobar una suma
    def test_add_method(self):
    # Ejecutamos el método
        self.calc.add(1, 3)
    # Comprobamos si el valor es el que esperamos
        self.assertEqual(4, self.calc.value)