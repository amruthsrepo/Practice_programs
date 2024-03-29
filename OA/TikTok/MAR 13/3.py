# Given a grid with n rows and m columns, count the number of possible placements for three knights on the grid such that no two knights' placements counter each other. Note that no two knights can be placed in the same cell.
# It is known that a knight in chess can counter another piece in cell (a2, b2) from the cell (a1, y1) if either (|a1 - a2| = 1 and |b1 - b2| = 2), or (|a1 - a2| = 2 and |b1 - b2| = 1).

# UL, UR, DL, DR, RU, RD, LU, LD


def knightPlacement(n, m):
    total_positions = n * m

    def is_valid_position(pos1, pos2):
        a1, b1 = pos1
        a2, b2 = pos2
        return (abs(a1 - a2) == 1 and abs(b1 - b2) == 2) or (
            abs(a1 - a2) == 2 and abs(b1 - b2) == 1
        )

    count = 0
    for i in range(total_positions):
        for j in range(i + 1, total_positions):
            for k in range(j + 1, total_positions):
                pos1 = (i // m, i % m)
                pos2 = (j // m, j % m)
                pos3 = (k // m, k % m)

                if (
                    not is_valid_position(pos1, pos2)
                    and not is_valid_position(pos1, pos3)
                    and not is_valid_position(pos2, pos3)
                ):
                    count += 1

    return count

    totalPlacements = 0
    for i in range(n):
        for j in range(m):
            totalPlacements += findPlacements(i, j)

    return totalPlacements


print(knightPlacement(2, 3))
