# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        resto = 0

        while l1 or l2 or resto:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            somma = val1 + val2 + resto
            resto = somma // 10
            cifra = somma % 10

            curr.next = ListNode(cifra)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next