class Solution(object):
    def isValidSudoku(self, board):
        for r in board:
            vals = [True] * 9
            for num in r:
                if num == '.': continue
                num = int(num) - 1
                vals[num] = not vals[num]
                if vals[num]:
                    print(1)
                    return False
        for j in range(9):
            vals = [True] * 9
            for i in range(9):
                num = board[i][j]
                if num == '.': continue
                num = int(num) - 1
                vals[num] = not vals[num]
                if vals[num]:
                    print(2)
                    return False
        for columnBlock in range(0,3,3):
            for rowBlock in range(0,3,3):
                vals = [True] * 9
                print('new block')
                for column in range(3):
                    for row in range(3):
                        num = board[rowBlock+row][columnBlock+column]
                        print(num, end='')
                        if num == '.': continue
                        num = int(num) - 1
                        vals[num] = not vals[num]
                        if vals[num]:
                            print(3)
                            return False
        return True