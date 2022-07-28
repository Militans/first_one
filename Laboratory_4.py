# def sin_a(r):
#     l = 0.28
#     a = (r ** 2 + l ** 2) ** 0.5
#     return r / a
# r = float(input("Введите R: "))
# r *= 10 ** -3
# print(sin_a(r))


# def sin_a(r):
#     l = 300
#     a = (r ** 2 + l ** 2) ** 0.5
#     return r / a
# r = float(input("Введите R: "))
# r *= 10 ** -3
# print(sin_a(r))


# def d(m, sin_a):
#     lamb = 6.5 * 10 ** -7
#     return (m * lamb) / sin_a
#
#
# m = int(input("Введите М: "))
# sin_a = float(input("Введите sin_a: "))
#
# print(d(m, sin_a) * 10 ** 6)


# def epsilon(r):
#     L = 0.28
#     delta_l = 0.001
#     delta_r = 0.001
#     a = (L ** 2) / (r ** 2 + L ** 2)
#     b = (delta_l / L) + (delta_r / r)
#     return a * b
#
#
# r = int(input("Введите R: "))
# r *= 10 ** -3
#
# print(epsilon(r))


# def delta_d(ep, d):
#     return ep * d
#
#
# ep, d = map(float, input().split())
# print(delta_d(ep, d))


# a = []
# for i in range(10):
#     t = float(input())
#     a.append(t)
# print(sum(a) / 10)
