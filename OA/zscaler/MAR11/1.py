def countSentences(wordSet, sentences):

    anaCount = {}

    for word in wordSet:
        sortedWord = "".join(sorted(word))
        anaCount[sortedWord] = anaCount.get(sortedWord, 0) + 1

    sentenceCount = []

    for sentence in sentences:
        currCount = 1
        for word in sentence.split(" "):
            sortedWord = "".join(sorted(word))
            currCount *= anaCount.get(sortedWord, 1)
        sentenceCount.append(currCount)

    return sentenceCount


print(countSentences(["listen", "silent", "it", "is"], ["listen it is silent"]))
print(
    countSentences(
        ["the", "bats", "tabs", "in", "cat", "act"],
        ["cat the bats", "in the act", "act tabs in"],
    )
)
