def findAllPrimes(limit):
    halfLimit = (limit + 1) // 2
    marked = [0] * halfLimit

    for i in range(1, halfLimit + 1):
        if ((i + 1) * (2 * i)) >= halfLimit:
            break
        for j in range(1, halfLimit + 1):
            toMark = (i + j) * (2 * i * j)
            print(toMark)
            if toMark >= halfLimit:
                break
            marked[toMark] = 1

    primes = [2]

    for i in range(1, len(marked)):
        if not marked[i]:
            primes.append(1 + (2 * i))

    return primes


print(findAllPrimes(20))
print(findAllPrimes(21))
print(findAllPrimes(22))
print(findAllPrimes(23))
