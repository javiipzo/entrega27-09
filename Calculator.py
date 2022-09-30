class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, a, b):
        self.value = a + b
    def multiply(self, a, b):
        self.value = a * b
    def divide(self, a, b):
        self.value = a / b
    def factorial(self,numero):
        fact = 1
        for i in range(1,numero+1):
            fact = fact * i
        self.value=fact