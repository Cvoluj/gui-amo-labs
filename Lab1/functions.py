from math import sqrt

class CalculationError(Exception):
    pass

def calculate_y1(a, c):
    results = []
    for i in range(min(len(a), len(c))):
        try:
            total = a[i] + c[i]
            if total == 0:
                raise CalculationError(f"Division by zero, a[{i}] + c[{i}] can't be equal to 0")
            elif total < 0:
                raise CalculationError(f"Square root of a[{i}] + c[{i}] must be greater or equal to 0")
            results.append(sqrt(total) + 1 / total)
        except CalculationError as ce:
            raise ce
    return results

def find_roots(*args):
    # 57.567 * x ** 2 - 11.675 * x - 34.114 = 0
    a = 57.567
    b = - 11.675
    c = - 34.114
    sqrtD = sqrt(b ** 2 - 4 * a * c)
    if sqrtD < 0:
        print('There are no real answers')
        return None, None
    return (-b + sqrtD)/(2 * a), (-b - sqrtD)/(2 * a)

def calculate_f(a, c, g, i=0):
    def recursive_f(a, c, g, i=0):
        if len(a) < 11 or len(c) < 11 or len(g) < 11:
            raise CalculationError(f'All lists must have at least 11 elements')

        if i > 10:
            return 0
        else:
            calc: float = round((a[i] ** 2 + 56 * c[i] * recursive_f(a, c, g, i + 1) * g[i]), 7)
            result.append(calc)
            return calc
    result = list()
    recursive_f(a, c, g, i)
    return result


if __name__ == '__main__':
    # print(calculate_y1([3, -1, -2, -1], [4, 1, -2, -1]))
    # x1, x2 = find_roots()
    # print(x1, x2)

    a_values = [float(0.2) for i in range(11)]
    c_values = [float(0.2) for i in range(11)]
    g_values = [float(0.2) for i in range(11)]

    print(calculate_f(a_values, c_values, g_values))
