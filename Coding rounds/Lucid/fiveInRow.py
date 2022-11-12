w, b = set(), set()


def o(x, y, s, u, v, n=0):
    if (x, y) in s:
        return o(x + u, y + v, s, u, v, n + 1)
    return n


def W(m, s):
    for (u, v) in ((0, 1), (1, 0), (1, 1), (-1, 1)):
        (x, y) = m
        rowLen = o(x + u, y + v, s, u, v) + o(x - u, y - v, s, -u, -v) + 1
        print(rowLen, end="")
        if rowLen > 4:
            print("")
            return 1
    print("")
    return 0


def t(c, p):
    while 1:
        C = input(c + ">")
        try:
            x, y = C.split()
            m = (int(x), int(y))
        except ValueError:
            continue
        if m in b or m in w:
            continue
        p.add(m)
        if W(m, p):
            print(c, "wins!")
            exit()
        break


while 1:
    t("b", b), t("w", w)
