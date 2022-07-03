# def n(p1, p2, d, t, l):
#     g = 9.8
#     k = ((p1 - p2) * g * (d ** 2) * t) / (18 * l)
#     return k
# p1 = 11.3 * (10 ** 3)
# p2 = 1.26 * (10 ** 3)
# p_2 = 0.9 * (10 ** 3)
# d = float(input('Введите диаметр шарика '))
# d *= 10 ** (-3)
# t = float(input('Введите время падения шарика '))
# l = 0.25
# print(n(p1, p_2, d, t, l))


def sigma_n(sigma_d, d, t, n):
    a = (2 * sigma_d) / d
    b = 0.01 / t
    l = 0.25
    c = 0.001 / l
    return (a + b + c) * n


sigma_d = float(input("Введите полную погрешность диаметра шарика "))
d = float(input("Введите диаметр шарика "))
t = float(input("Введите время "))
n = float(input("Введите вязкость, вычисленную ранее "))
print(sigma_n(sigma_d, d, t, n))
