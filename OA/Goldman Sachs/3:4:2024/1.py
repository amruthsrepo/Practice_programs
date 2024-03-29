def plusMult(A):
    lenA = len(A)
    rEven = A[0]
    rOdd = A[1]
    even, odd = 2, 3
    multi = True

    while even < lenA or odd < lenA:
        if even < lenA:
            if multi:
                rEven *= A[even]
            else:
                rEven += A[even]
        if odd < lenA:
            if multi:
                rOdd *= A[odd]
            else:
                rOdd += A[odd]
        even += 2
        odd += 2

    rEven %= 2
    rOdd %= 2

    if rOdd == rEven:
        return "NEUTRAL"
    elif rOdd > rEven:
        return "ODD"
    return "EVEN"


print(plusMult([12, 3, 5, 7, 13, 12]))
print(plusMult([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(plusMult([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
