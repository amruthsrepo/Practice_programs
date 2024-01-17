def getTotalEfficiency(skill):
    skill.sort()

    numSkill = len(skill)
    efficiency = 0
    target_sum = skill[0] + skill[-1]

    for i in range(numSkill // 2):
        if skill[i] + skill[numSkill - 1 - i] != target_sum:
            return -1
        efficiency += skill[i] * skill[numSkill - 1 - i]

    return efficiency


print(getTotalEfficiency([1, 2, 3, 2]))
print(getTotalEfficiency([5, 4, 2, 1]))
print(getTotalEfficiency([2, 1, 1, 4, 3, 5]))
