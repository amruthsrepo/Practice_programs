def calculateValidity(arr):

    validity = float("inf")
    dp = set()
    start = 0

    for end in range(3, len(arr) + 1):
        a, b, c = sorted(arr[start:end])
        if (a, b, c) in dp:
            continue
        else:
            mean = round(((a + b + c) / 3), 2)
            absolute = round(abs(mean - b), 2)
            tempValidity = 3 * absolute
            rem = tempValidity % 1
            tempValidity = int((tempValidity // 1) + (rem > 0))
            dp.add((a, b, c))
        validity = (validity, tempValidity)[validity > tempValidity]
        start += 1

    return validity


print(calculateValidity([1, 2, 4]))
print(calculateValidity([2, 3, 1, 4]))
print(calculateValidity([20, 15, 99, 100]))
# print(calculateValidity([20, 15, 99, 100]))
