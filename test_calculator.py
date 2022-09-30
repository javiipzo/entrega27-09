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

    def test_multiply_method(self):
        self.calc.multiply(2, 3)
        self.assertEqual(6, self.calc.value)
    def test_divide_method(self):
        self.calc.divide(8,2)
        self.assertEqual(4, self.calc.value)
    def test_factorial_method(self):
        self.calc.factorial(4)
        self.assertEqual(24,self.calc.value)