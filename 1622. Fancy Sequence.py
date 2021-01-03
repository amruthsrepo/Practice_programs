class Fancy:

    def __init__(self):
        self.seqObj = []
        self.expLhs, self.expRhs = [], []
        self.numOperations = 0

    def append(self, val: int) -> None:
        self.seqObj.append([val, self.numOperations])

    def addAll(self, inc: int) -> None:
        self.expLhs.append('(')
        self.expRhs.append('+' + repr(inc) + ')')
        self.numOperations += 1

    def multAll(self, m: int) -> None:
        self.expLhs.append('(')
        self.expRhs.append('*' + repr(m) + ')')
        self.numOperations += 1

    def getIndex(self, idx: int) -> int:
        try:
            exp = ''
            exp = exp.join(self.expLhs[self.seqObj[idx][1]:])
            exp += repr(self.seqObj[idx][0])
            exp += ''.join(self.expRhs[self.seqObj[idx][1]:])
            return eval(exp)
        except:
            return -1


obj = Fancy()
obj.append(12)
obj.append(8)
print(obj.getIndex(1))
obj.append(12)
print(obj.getIndex(0))
obj.addAll(12)
obj.append(8)
print(obj.getIndex(2))
print(obj.getIndex(2))
obj.append(4)
obj.append(13)
print(obj.getIndex(4))
obj.append(12)
print(obj.getIndex(6))
obj.append(11)
print(obj.getIndex(1))
obj.append(10)
print(obj.getIndex(2))
obj.multAll(3)
obj.addAll(1)
print(obj.getIndex(6))
obj.append(14)
obj.addAll(5)
print(obj.getIndex(6))
obj.multAll(12)
print(obj.getIndex(3))
obj.multAll(12)
obj.addAll(15)
obj.addAll(6)
obj.append(7)
obj.multAll(8)
obj.append(13)
obj.append(15)
obj.append(15)
obj.multAll(10)
print(obj.getIndex(9))
obj.multAll(12)
obj.multAll(12)
obj.multAll(9)
print(obj.getIndex(9))
obj.addAll(9)
obj.append(9)
obj.multAll(4)
obj.addAll(8)
obj.addAll(11)
obj.multAll(15)
obj.addAll(9)
obj.addAll(1)
obj.append(4)
obj.append(10)
print(obj.getIndex(9))
