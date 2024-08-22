#john sebastian peña sanchez
import math

def suma(c1, c2):
    """Suma dos números complejos c1 y c2."""
    return (c1[0] + c2[0], c1[1] + c2[1])

def resta(c1, c2):
    """Resta dos números complejos c1 y c2."""
    return (c1[0] - c2[0], c1[1] - c2[1])

def producto(c1, c2):
    """Multiplica dos números complejos c1 y c2."""
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imaginario = c1[0] * c2[1] + c1[1] * c2[0]
    return (real, imaginario)

def division(c1, c2):
    """Divide el número complejo c1 entre c2."""
    divisor = c2[0] ** 2 + c2[1] ** 2
    real = (c1[0] * c2[0] + c1[1] * c2[1]) / divisor
    imaginario = (c1[1] * c2[0] - c1[0] * c2[1]) / divisor
    return (real, imaginario)

def modulo(c):
    """Retorna el módulo de un número complejo c."""
    return math.sqrt(c[0] ** 2 + c[1] ** 2)

def conjugado(c):
    """Retorna el conjugado de un número complejo c."""
    return (c[0], -c[1])

def cartesiano_a_polar(c):
    """Convierte un número complejo de coordenadas cartesianas a polares."""
    magnitud = modulo(c)
    fase = math.atan2(c[1], c[0])
    return (magnitud, fase)

def polar_a_cartesiano(p):
    """Convierte un número complejo de coordenadas polares a cartesianas."""
    real = p[0] * math.cos(p[1])
    imaginario = p[0] * math.sin(p[1])
    return (real, imaginario)

def fase(c):
    """Retorna la fase (ángulo) de un número complejo c."""
    return math.atan2(c[1], c[0])
