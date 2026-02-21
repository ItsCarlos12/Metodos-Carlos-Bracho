"""Funciones a analizar con los distintos métodos numéricos.

El programa principal (examen-2.py) detecta automáticamente
las funciones definidas aquí para que puedas elegirlas.
"""

import math


def f_biseccion(x: float) -> float:
	"""Función para el método de bisección.

	Ecuación: f(x) = x**3 - 12x - 141 = 0
	"""
	return x**3 - 12 * x - 141


def f_regula(t: float) -> float:
	"""Función para el método de regula falsi.

	Ecuación: f(t) = 35 + (95 - 35)e**(-0.057 t) - 46 = 0
	Se implementa como: 35 + 60*exp(-0.057*t) - 46
	"""
	return 35 + (95 - 35) * math.exp(-0.057 * t) - 46


def f_newton(x: float) -> float:
	"""Función para el método de Newton-Raphson.

	Ecuación: f(x) = x**2 - 4.30 * ln(x + 1) - 5 = 0
	"""
	return x**2 - 4.30 * math.log(x + 1) - 5


def df_newton(x: float) -> float:
	"""Derivada de f_newton(x) para Newton-Raphson.

	Para f(x) = x**2 - 4.30*ln(x+1):
	f'(x) = 2x - 4.30 / (x + 1)
	"""
	return 2 * x - 4.30 * (1.0 / (x + 1))


def f_secante(R: float) -> float:
	"""Función para el método de la secante.

	Ecuación: f(R) = R * e**(0.1 R) - 4.43 = 0
	"""
	return R * math.exp(0.1 * R) - 4.43

