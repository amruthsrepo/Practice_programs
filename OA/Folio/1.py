def Main(arg):
    letterLoc = {}
    start = 0
    longest = 1 if arg else 0

    for ind, letter in enumerate(arg):
        if letter in letterLoc:
            longest = max(longest, len(letterLoc))
            while letter in letterLoc:
                del letterLoc[arg[start]]
                start += 1
        letterLoc[letter] = ind

    longest = max(longest, len(letterLoc))
    return longest


print(Main("pwwkew"))
print(Main("ababc"))
