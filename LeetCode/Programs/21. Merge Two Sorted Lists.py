# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        retList = retNext = ListNode()
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                retNext.next = list1
                list1 = list1.next
                retNext = retNext.next
            else:
                retNext.next = list2
                list2 = list2.next
                retNext = retNext.next
        if list1:
            retNext.next = list1
        elif list2:
            retNext.next = list2
        return retList.next