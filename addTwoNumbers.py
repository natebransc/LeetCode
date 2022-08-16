# LeetCode practice problem
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []

        while l1 is not None:
            v1 = l1.val
            list1.append(v1)
            l1 = l1.next

        while l2 is not None:
            v2 = l2.val
            list2.append(v2)
            l2 = l2.next

        s1 = ""
        s2 = ""

        size = len(list1)
        i = 1
        while abs(i) <= size:
            s1 += str(list1[-i])
            i += 1

        size = len(list2)
        i = 1
        while abs(i) <= size:
            s2 += str(list2[-i])
            i += 1

        sum = int(s1) + int(s2)
        sumStr = str(sum)

        head = ListNode(int(sumStr[-1]))
        cheatSheet = []
        cheatSheet.append(head)
        i = 2

        while i <= len(sumStr):
            node = ListNode(int(sumStr[-i]))
            cheatSheet[i - 2].next = node
            cheatSheet.append(node)
            i += 1

        return head

sol = Solution

h1 = ListNode(0)

h2 = ListNode(0)


sol = Solution
ans = sol.addTwoNumbers(sol, h1, h2)
print(ans.val)