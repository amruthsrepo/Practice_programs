def getTotalEfficiency(skill):
    if (len(skill) % 2) > 0:
        return -1

    avgEfficiency = sum(skill) / (len(skill) / 2)
    if (avgEfficiency % 1) > 0:
        return -1

    skillCount = {}
    for c in skill:
        skillCount[c] = skillCount.get(c, 0) + 1

    totalEfficiency = 0
    for c in skillCount:
        if not skillCount[c]:
            continue

        cRem = avgEfficiency - c
        if not skillCount[c] == skillCount.get(cRem, 0):
            return -1
        else:
            if c == cRem:
                totalEfficiency += (skillCount[c] // 2) * c * cRem
            else:
                totalEfficiency += skillCount[c] * c * cRem
            skillCount[c] = 0
            skillCount[cRem] = 0

    return int(totalEfficiency)


print(getTotalEfficiency([1, 3, 2, 2]))
print(getTotalEfficiency([5, 4, 2, 1]))
print(getTotalEfficiency([2, 1, 1, 4, 3, 5]))
