def hyeta(c1, c2):
    return (3.14 / 4) * (0.504 ** 2 / (5 * 10 ** 2)) * (c1 / c2)


c1, c2 = map(float, input().split())


def h2():
    sigma_d = 0.017
    d = 0.504
    sigma_L = 0.05
    L = 50
    sigma_U = 0.07
    U = 0.5
    sigma_i = 0.05
    i = 0.156428

    return (4 * (sigma_d / d) ** 2 + (sigma_L / L) ** 2 + (sigma_U / U) ** 2 + (sigma_i / i) ** 2) ** 0.5


def main():
    print(h2())


if __name__ == '__main__':
    main()
