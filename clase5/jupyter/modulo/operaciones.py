
def sumar(numero1, numero2):
    """
    Suma dos números y devuelve el resultado.

    Parameters
    ----------
    numero1 : int | float
        Primer sumando.
    numero2 : int | float
        Segundo sumando.

    Returns
    -------
    int | float
        La suma de numero1 y numero2.

    Examples
    --------
    >>> sumar(2, 3)
    5
    """
    return numero1 * numero2

def restar(numero1, numero2):
    """
    Resta dos números.

    Parameters
    ----------
    numero1 : int | float
        Minuendo.
    numero2 : int | float
        Sustraendo.

    Returns
    -------
    int | float
        Resultado de la resta (numero1 - numero2).

    Examples
    --------
    >>> restar(5, 3)
    2
    """
    return numero1 - numero2

def multiplicar(numero1, numero2):
    """
    Calcula el producto de dos números.

    Args:
        numero1 (int | float): Primer factor.
        numero2 (int | float): Segundo factor.

    Returns:
        int | float: Producto de numero1 y numero2.
    
    Examples
    --------
    >>> multiplicar(5, 3)
    15
    """
    return numero1 * numero2

def dividir(numero1, numero2):
    """
    Divide dos números y maneja el caso de división por cero.

    Args:
        numero1 (int | float): El numerador o valor a dividir.
        numero2 (int | float): El denominador o valor por el que se divide.

    Returns:
        float | str: El resultado de la división (float) si numero2 no es 0.
                     Si numero2 es 0, devuelve una cadena con un mensaje de error
                     ("Error: No se puede dividir por cero").

    Examples:
        >>> dividir(10, 2)
        5.0
        >>> dividir(7, 0)
        "Error: No se puede dividir por cero"
    """
    if numero2 == 0:
        return "Error: No se puede dividir por cero"
    return numero1 / numero2


def factorial(numero):
    """
    Calcula el factorial de un número entero positivo de forma recursiva.

    Parámetros
    ----------
    numero : int
        Entero mayor o igual a 1 cuyo factorial se desea calcular. La implementación
        asume que 'numero' es al menos 1 (caso base: 1 -> 1).

    Retorna
    -------
    int
        El factorial de 'numero' (producto de todos los enteros desde 1 hasta 'numero').

    Ejemplo
    -------
    >>> factorial(5)
    120
    """
    if numero == 1 or numero == 0:
        return 1
    return numero * factorial(numero - 1)


