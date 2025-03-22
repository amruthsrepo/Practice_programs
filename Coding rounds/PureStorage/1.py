def count_palindromes(S):
    numLetters = len(S)
    palindromeTable = [[False] * numLetters for _ in range(numLetters)]
    totalPalindromes = 0

    for i in range(numLetters):
        palindromeTable[i][i] = True
        totalPalindromes += 1

    for i in range(numLetters - 1):
        if S[i] == S[i + 1]:
            palindromeTable[i][i + 1] = True
            totalPalindromes += 1

    for length in range(3, numLetters + 1):
        for i in range(numLetters - length + 1):
            if S[i] == S[i + length - 1] and palindromeTable[i + 1][i + length - 2]:
                palindromeTable[i][i + length - 1] = True
                totalPalindromes += 1

    return totalPalindromes


print(count_palindromes("hellolle"))
print(count_palindromes("wowpurerocks"))
