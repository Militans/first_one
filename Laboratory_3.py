def ro(U, I):
    d = 0.432 * 10 ** (-3)
    pi = 3.14
    l = 0.5
    return (U / I) * ((pi * (d ** 2)) / (4 * l))


# U, I, = map(float, input().split())
# print(ro(U, I))
# print(0.25 / ((3.14 * (0.432 * 10 ** (-3)) ** 2) / 4))


def V_dr(j, e, n):
    return j / (e * n)


j = 1.7 * 10 ** 6
e = 1.16 * 10 ** (-19)
n = 0.871 * 10 ** (23)


# print(V_dr(j, e, n))


def V_sr_temp():
    k = 1.38 * 10 ** (-23)
    T = 300
    pi = 3.14
    m = 9.1 * 10 ** (-31)
    return ((8 * k * T) / (pi * m)) ** 0.5


# print(V_sr_temp())
# print(1.8 / (1.7 * 10 ** (6)))


def sigmaro(sigma_d, d, sigma_l, l, sigma_u, u, sigma_i, i):
    Ro = 1.02 * 10 ** (-6)
    a = (sigma_d / d) ** 2
    b = (sigma_l / l) ** 2
    c = (sigma_u / u) ** 2
    d = (sigma_i / i) ** 2
    return (4 * a * b * c * d) ** 0.5 * Ro


print(sigmaro(0.02, 0.432, 0.01, 0.5, 0.025, 0.89, 0.025, 0.25))
