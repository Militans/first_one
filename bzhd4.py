import math as mt


def f_0(c, m):
    pi = mt.pi
    return (1 / (2 * pi)) * ((c / m) ** 0.5)


def f_v(n_y):
    return n_y / 60


def delta_l(a):
    if a <= 15:
        return 17
    elif (a >= 20) and (a <= 60):
        return 20
    else:
        return 26


def f_od(a, b):
    return a / b


def F_v(m_o, low_sigma):
    return 9.81 * m_o / low_sigma


def sigma_Kv(a, m_0):
    return 4 * mt.pi ** 2 * a ** 2 * m_0


def Hp(E, F_v, sigmaKv):
    return E * F_v / sigmaKv


def delta_ly(a, b):
    return 20 * mt.log10((a ** 2 / b ** 2) - 1)


def main():
    n_y = 1400
    m_v = 35
    E = 25 * 10 ** 5
    m_o = 270
    n_v = 4
    P = 4.5
    epsilon = 0.2
    low_sigma = 3 * 10 ** 5
    L_k = 88

    a = f_v(n_y)
    print(f"f_v = {a}, Гц")
    b = f_od(a, 4.2)
    print(f"f_od = {b}, Гц")
    sigmaKv = sigma_Kv(b, m_o)
    print(f"sigmaK_v = {sigmaKv}, H/m")
    F_V = F_v(m_o, low_sigma)
    print(f"F_v = {F_V}, М^2")
    f_1 = F_V / n_v
    print(f"f_1 = {f_1}, m^2")
    B = f_1 ** 0.5
    print(f"B = {B}, m")
    print((1.5 * Hp(E, F_V, sigmaKv) <= B) and (B <= 8 * Hp(E, F_V, sigmaKv)))
    D = (4 * f_1 / mt.pi) ** 0.5
    print((1.5 * Hp(E, F_V, sigmaKv) <= D) and (D <= 8 * Hp(E, F_V, sigmaKv)))
    H = Hp(E, F_V, sigmaKv) + 0.125 * B
    Sigma_k = E * F_V / Hp(E, F_V, sigmaKv)
    F_0 = f_0(Sigma_k, m_o)
    print(f"F_0 = {F_0}, Гц")
    delta_LY = delta_ly(a, F_0)
    L = L_k - delta_LY
    print(L)


if __name__ == "__main__":
    main()
