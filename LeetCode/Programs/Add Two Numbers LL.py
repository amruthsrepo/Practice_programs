# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list2Node(l: list):
    retList = lN = ListNode(l[0])
    for i in range(1, len(l)):
        lN.next = ListNode(l[i])
        lN = lN.next
    return retList


def node2Str(lN: ListNode):
    l = ''
    while lN:
        l = repr(lN.val) + l
        lN = lN.next
    return l


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1.val += l2.val
        carry = int(l1.val/10)
        l1.val = l1.val % 10
        last = l1
        retlist, l1, l2 = l1, l1.next, l2.next
        while l1 or l2 or carry > 0:
            if l1 and l2:
                l1.val += (l2.val + carry)
                carry = int(l1.val/10)
                l1.val = l1.val % 10
                last = l1
                l1, l2 = l1.next, l2.next
            elif l1:
                l1.val += carry
                carry = int(l1.val/10)
                l1.val = l1.val % 10
                last = l1
                l1 = l1.next
            elif l2:
                last.next = l1 = l2
                l2 = None
                l1.val += carry
                carry = int(l1.val/10)
                l1.val = l1.val % 10
                last = l1
                l1 = l1.next
            else:
                last.next = ListNode(carry)
                break
        return retlist


l1, l2 = list2Node([0]), list2Node([7, 3])
s = Solution()
ans = s.addTwoNumbers(l1, l2)
print(node2Str(ans))
