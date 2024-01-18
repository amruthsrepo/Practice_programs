def compareStrings(s1, s2):
    stack1, stack2 = "", ""

    for c in s1:
        if c == "#":
            stack1 = stack1[:-1]
        else:
            stack1 += c

    for c in s2:
        if c == "#":
            stack2 = stack2[:-1]
        else:
            stack2 += c

    if stack1 == stack2:
        return 1

    return 0


print(compareStrings("axx#bb#c", "axbd#c#c"))
print(compareStrings("yf#c#", "yy#k#pp##"))
print(compareStrings("hacc#kk#", "hb##acKK##"))
