# class MinStack(object):
#     class Node:
#         def __init__(self, x = None):
#             self.val = x
#             self.min = x
#             self.prev = None

#     def __init__(self):
#         self.topNode = None

#     def push(self, val):
#         temp = self.Node(val)
#         if self.topNode != None:
#             temp.prev = self.topNode
#             temp.min = min(val, self.topNode.min)
#         self.topNode = temp

#     def pop(self):
#         temp = self.topNode
#         self.topNode = self.topNode.prev
#         del temp

#     def top(self):
#         if self.topNode == None:
#             return None
#         else:
#             return self.topNode.val

#     def getMin(self):
#         if self.topNode == None:
#             return None
#         else:
#             return self.topNode.min


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minVals = []
        self.stackSize = 0

    def push(self, val):
        self.stack.append(val)
        self.stackSize += 1
        if self.stackSize > 1:
            self.minVals.append(min(val,self.minVals[-1]))
        else:
            self.minVals.append(val)

    def pop(self):
        if self.stackSize > 0:
            self.stack.pop()
            self.minVals.pop()
            self.stackSize -= 1

    def top(self):
        if self.stackSize > 0:
            return self.stack[-1]
        return None

    def getMin(self):
        if self.stackSize > 0:
            return self.minVals[-1]
        return None



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())