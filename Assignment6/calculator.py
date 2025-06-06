

class Calculator():
    
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if (x > 0 and y == 0):
            raise ZeroDivisionError("Cannot divide by 0")
        else:
            return x / y
        
