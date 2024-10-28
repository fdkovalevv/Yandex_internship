def find_min_mn(a, b, c, d):
    options = []

    m1 = max(a, b) + 1
    n1 = 1
    if m1 <= a+b:
        options.append((m1, n1))

    m2 = a + 1
    n2 = c + 1
    if m2 <= a + b and n2 <= c + d:
        options.append((m2, n2))

    m3 = b + 1
    n3 = d + 1
    if m3 <= a + b and n3 <= c + d:
        options.append((m3, n3))

    m4 = 1
    n4 = max(c, d) + 1
    if n4 <= c+d:
        options.append((m4, n4))

    minn = float("inf")
    res = (0, 0)
    for i in options:
        m, n = i
        if m < 1 and n < 1:
            continue
        summ = m + n
        if summ < minn:
            minn = summ
            res = (m, n)
        elif summ == minn:
            if m > res[0]:
                res = (m, n)
    return res

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(*find_min_mn(a, b, c, d))











