def sum(a, b):
    """Retorna la suma de dos números."""
    '''
    >>> sum(2, 3)
    5
    '''
    return a + b

def subtract(a, b):
    """Retorna la resta de dos números."""
    return a - b

def multiply(a, b):
    """Retorna el producto de dos números."""
    return a * b

def divide(a, b):
    '''
    >>> divide(10, 0)
    Traceback (most recent call last):
    ZeroDivisionError: No se puede dividir por cero
    '''
    """Retorna la división de dos números."""
    if b ==0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

