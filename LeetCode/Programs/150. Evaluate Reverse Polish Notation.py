
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numStack = []
        validOperators = '+-/*'
        for t in tokens:
            if t in validOperators:
                r,l = numStack.pop(), numStack.pop()
                if t == '+':
                    numStack.append(l + r)
                elif t == '-':
                    numStack.append(l - r)
                elif t == '*':
                    numStack.append(l * r)
                else:
                    numStack.append(int(l / float(r)))
            else:
                numStack.append(int(t))
        return numStack.pop()


s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(s.evalRPN(["2","1","+","3","*"]))
print(s.evalRPN(["4","13","5","/","+"]))
