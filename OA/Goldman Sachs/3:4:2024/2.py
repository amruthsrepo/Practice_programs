def doesCircleExist(commands):

    for command in commands:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, dir_idx = 0, 0, 0

        for instruction in command:
            if instruction == "G":
                dx, dy = directions[dir_idx]
                x, y = x + dx, y + dy
            elif instruction == "L":
                dir_idx = (dir_idx - 1) % 4
            elif instruction == "R":
                dir_idx = (dir_idx + 1) % 4

        if (x, y) == (0, 0) or dir_idx != 0:
            print("YES")
        else:
            print("NO")


doesCircleExist(["GRGL"])
doesCircleExist(["R"])
doesCircleExist(["L"])
doesCircleExist(["GR"])
doesCircleExist(["G"])
