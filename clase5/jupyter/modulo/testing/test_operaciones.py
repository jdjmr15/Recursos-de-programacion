"""Genera el archivo de pruebas para la calculadora para el modeulo de operaciones"""

from modulo.operaciones import sumar, restar, multiplicar

def test_sumar():
    """Prueba la función sumar"""
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
    assert sumar(2.5, 3.5) == 6.0

def test_restar():
    """Prueba la función restar"""
    assert restar(5, 3) == 2
    assert restar(0, 0) == 0
    assert restar(-1, -1) == 0
    assert restar(3.5, 2.5) == 1.0

def test_multiplicar():
    """Prueba la función multiplicar"""
    assert multiplicar(5, 3) == 15
    assert multiplicar(0, 10) == 0
    assert multiplicar(-2, 3) == -6
    assert multiplicar(2.5, 4) == 10.0
