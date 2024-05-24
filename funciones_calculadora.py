import math

def sumar(a, b):
    """Calcula la suma de dos números.
    
    Args:
        a (float): Primer número.
        b (float): Segundo número.
    
    Returns:
        float: Resultado de la suma.
    """
    return a + b

def restar(a, b):
    """Calcula la resta de dos números.
    
    Args:
        a (float): Primer número.
        b (float): Segundo número.
    
    Returns:
        float: Resultado de la resta.
    """
    return a - b

def dividir(a, b):
    """Calcula la división de dos números.
    
    Args:
        a (float): Primer número.
        b (float): Segundo número.
    
    Returns:
        float: Resultado de la división, o un mensaje de error si b es cero.
    """
    if b == 0:
        return "No es posible dividir por cero"
    return a / b

def multiplicar(a, b):
    """Calcula la multiplicación de dos números.
    
    Args:
        a (float): Primer número.
        b (float): Segundo número.
    
    Returns:
        float: Resultado de la multiplicación.
    """
    return a * b

def factorial(n):
    """Calcula el factorial de un número.
    
    Args:
        n (int): Número entero.
    
    Returns:
        int: Factorial del número.
    """
    if n < 0:
        return "Factorial no definido para números negativos"
    return math.factorial(n)