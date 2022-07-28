def perevod(n):
    arr = ['A', 'B', 'C', 'D', 'E', 'F']
    s = ''
    while n != 0:
        t = n % 16
        if n >= 10:
            s += arr[t % 10]
        else:
            s += str(t)
        n //= 16
    return s[::-1]
# print(perevod(123))
