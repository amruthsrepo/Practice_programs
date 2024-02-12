def solution(N, S):

    if not S:
        return N * 2

    S = set(S.split(" "))
    maxFamilies = 0

    for row in range(1, N + 1):
        b = str(row) + "B" in S
        c = str(row) + "C" in S
        d = str(row) + "D" in S
        e = str(row) + "E" in S
        f = str(row) + "F" in S
        g = str(row) + "G" in S
        h = str(row) + "H" in S
        j = str(row) + "J" in S

        leftNotTaken = not (b + c + d + e)
        rightNotTaken = not (f + g + h + j)
        midNotTaken = not (d + e + f + g)

        maxFamilies += max(midNotTaken, leftNotTaken + rightNotTaken)

    return maxFamilies


print(solution(2, "1A 2F 1C"))
print(solution(30, "1A 3C 2B 20G 5A"))
print(solution(1, ""))
