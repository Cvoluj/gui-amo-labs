def equation(x):
    return (x ** 3) - x + 1


def bisection(a, b, expected_precision):
    precision = abs(b - a)

    while precision >= expected_precision:
        c = (a + b) / 2

        if equation(a) * equation(b) >= 0:
            return None
        elif equation(c) * equation(a) < 0:
            b = c
            precision = abs(b - a)
        elif equation(c) * equation(b) < 0:
            a = c
            precision = abs(b - a)
    return c
