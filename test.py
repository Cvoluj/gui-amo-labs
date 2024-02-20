def calculate_f(a, c, g, i=0):
    if i > 10:
        return 0
    else:
        calc: float = round((a[i] ** 2 + 56 * c[i] * calculate_f(a, c, g, i + 1) * g[i]), 7)
        print(calc)
        return calc
a_values = [float(0.2) for i in range(11)]
c_values = [float(0.2) for i in range(11)]
g_values = [float(0.2) for i in range(11)]

result = calculate_f(a_values, c_values, g_values)
print("Значення функції f:", result)