# A balanced sequence of parentheses is one in which every opening bracket has a corresponding closing bracket to it. More formally, a sequence of parantheses is Considered balanced if it can be represented in the form s1(2) where both s1 and s2 are either empty or balanced strings. Given a sequence of parentheses, find the minimum number of swaps needed to make the sequence balanced. It is not necessary to swap adjacent characters only. If it is impossible to balance the string, return -1.


def minimumSwaps(brackets):
    if len(brackets) % 2 != 0:
        return -1

    queue = []

    for bracket in brackets:
        if bracket == "(":
            queue.append(bracket)
        elif queue and queue[-1] == "(":
            queue.pop()
        else:
            queue.insert(0, bracket)

    numOpen = queue.count("(")

    if numOpen == (len(queue) - numOpen):
        return -(-numOpen // 2)
    else:
        return -1


print(minimumSwaps("(()))"))
print(minimumSwaps("())("))
print(minimumSwaps(")()("))
print(minimumSwaps(")()((("))
print(minimumSwaps("(()))(("))
