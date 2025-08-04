def sum(a, b):
    """Retorna la suma de dos números."""
    return a + b

def subtract(a, b):
    """Retorna la resta de dos números."""
    return a - b

def multiply(a, b):
    """Retorna el producto de dos números."""
    return a * b

def divide(a, b):
    """Retorna la división de dos números."""
    if b ==0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

