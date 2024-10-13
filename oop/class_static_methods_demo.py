#class_static_methods_demo.py
class Calculator:
    calculation_type = "Arithmetic Operations"

    #staticmethod
    @staticmethod
    def add(a, b):
        return a + b
    #classmethod
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b
