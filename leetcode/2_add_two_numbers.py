# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = temp = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            temp1 = l1.val if l1 else 0
            temp2 = l2.val if l2 else 0
            tempSum = temp1 + temp2 + carry

            temp.next = ListNode(tempSum % 10)
            temp = temp.next
            carry = tempSum // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next


if __name__ == '__main__':
    s = Solution()
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)

    node1.next = node2
    node2.next = node3

    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)

    node4.next = node5
    node5.next = node6

    result = s.addTwoNumbers(node1, node4)
    print result.val
    print result.next.val
    print result.next.next.val
