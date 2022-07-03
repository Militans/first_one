def random_error(a, a_mean, n):  # Вычисление средней случайной погрешности
    c = 0
    for i in a:
        c += abs(i - a_mean)
    k = c / n
    return k


def total_error(sistem_error, k):  # Вычисление полной погрешности
    return (sistem_error ** 2 + k ** 2) ** 0.5



a = []
n = int(input('Введите количество измерений '))
for i in range(n):
    t = float(input('Введите измерение '))
    a.append(t)
a_mean = sum(a) / len(a)

# sistem_error = float(input('Введите системную погрешность '))

#
p = random_error(a, a_mean, n)
print(p)
# print(total_error(sistem_error, p))  # вывод полной погрешности


def g(m, a):  # вычисление ускорения совбодного падения
    M = 453
    return (2 * M + m) / m * a


# m, a = map(float, input().split())
# print(g(m, a))


def a(h, t):  # Вычисление ускорения
    return 2 * h / (t ** 2)


#
# t, p = map(float, input().split())
# print(a(t, p))


def sigma_a(a, sigma_t, t):  # вычисление сигмы а
    sigma_h = 0.01
    h = 0.9
    b = sigma_h / h
    c = 2 * sigma_t / t
    return a * (b + c)


# a = float(input('Введите ускорение '))
# sigma_t = float(input('Введите сигму т '))
# t = float(input('Введите время '))
# print(sigma_a(a, sigma_t, t))


def sigma_g(m, sigma_a):  # вычисление сигмы G
    M = 453
    return (2 * M + m) / m * sigma_a


# #
# a = float(input('Введите массу груза '))
# b = float(input('Введите сигму а '))
# print(sigma_g(a, b))


def grafick(t):  # вычисление графиков
    return t ** 2 / 2
# print(grafick(float(input())))
