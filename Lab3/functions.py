import math
from typing import Any
from dataclasses import dataclass


@dataclass
class Point:
    x: Any
    y: Any


def sin_x(x):
    return math.sin(x)


def sin_x_square(x):
    return math.sin(x ** 2)


def lagrange_interpolation(f: list[Point], xi_list: list) -> list[float]:
    n = len(f)
    interpolated_list = []

    for xi in xi_list:
        result = 0
        for i in range(n):
            term = 1
            for j in range(n):
                if j != i:
                    term *= (xi - f[j].x) / (f[i].x - f[j].x)

            result += term * f[i].y
        interpolated_list.append(result)
    return interpolated_list
