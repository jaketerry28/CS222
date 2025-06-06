def fahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit-32) * (5.0/9.0)
    return round(celsius, 2)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        raise ValueError("Cannot be negative")
    else:
        return (n-1) + (n - 2)

