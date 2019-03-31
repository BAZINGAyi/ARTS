# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Notice
# 1. It should be carried from left to right
# 2. The L1 OR L2 can cloud be null.
# 3. The length of return list can be increased because of the carry
# 4. The length of list can be increased only when l1 and l2 are not empty.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def two_list_sum(l1: ListNode, l2: ListNode):

    result_list = ListNode(0)
    head = result_list
    carry = 0

    while l1 is not None or l2 is not None:

        l1_value = l1.val if l1 is not None else 0
        l2_value = l2.val if l2 is not None else 0

        sum = l1_value + l2_value + carry
        head.val = (sum % 10)
        carry = int(sum / 10)

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        if l1 or l2:
            new_node = ListNode(0)
            head.next = new_node
            head = head.next

    if carry is 1:
        head.next = ListNode(1)

    while result_list is not None:
        print(result_list.val)
        result_list = result_list.next


def htest_case1():
    a1 = ListNode(2)
    a2 = ListNode(4)
    a3 = ListNode(3)

    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(4)

    a1.next = a2
    a2.next = a3
    b1.next = b2
    b2.next = b3

    two_list_sum(a1, b1)


def htest_case2():
    a1 = ListNode(0)
    a2 = ListNode(1)

    b1 = ListNode(0)
    b2 = ListNode(1)
    b3 = ListNode(2)

    a1.next = a2
    b1.next = b2
    b2.next = b3

    two_list_sum(a1, b1)


def htest_case3():
    a1 = ListNode(1)

    b1 = ListNode(9)
    b2 = ListNode(9)
    b3 = ListNode(2)

    b1.next = b2
    b2.next = b3

    two_list_sum(a1, b1)


if __name__ == '__main__':

    htest_case1()

    print()

    htest_case2()

    print()

    htest_case3()