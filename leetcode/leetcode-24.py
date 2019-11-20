# Question: Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself
# may be changed.

# Example:
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head

        index = 0
        fake_head = ListNode(0)
        fake_head.next = head

        prev = fake_head
        current = head
        next = head.next

        while current.next is not None:
            if index % 2 is 0:
                prev.next = next
                current.next = next.next
                next.next = current

            else:
                prev = current
                current = current.next
                next = current.next

            index += 1

        return fake_head.next

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if head is None or head.next is None:
            return head

        list_length = 0
        new_head = head
        while new_head is not None:
            list_length += 1
            new_head = new_head.next
        count = int(list_length / k)
        if list_length < k:
             return head

        return self.swapPairs_Good(head, k, count)

    def swapPairs_Good(self, head: ListNode, k, count, current_count=0) -> ListNode:

        prev = None
        current = head
        n = k

        while current and n > 0:
            n -= 1
            next = current.next
            current.next = prev
            prev = current
            current = next
        current_count += 1

        if current is not None and current_count < count:
            head.next = self.swapPairs_Good(current, k, count,
                                            current_count=current_count)
        else:
            head.next = current
        return prev

    def reversed_node_list(self, pre: ListNode, current: ListNode, n):

        while current and n > 0:
            n -= 1
            next = current.next
            pre.next = next
            next.next = current
            current.next = prev
            prev = current
            current = next

        # if current.next is None or current_count > count:
        #     return fake_head.next
        # else:
        #     current_count += 1
        #     current.next = self.reversed_node_list(current.next)

    def print_list_node(self, head: ListNode):
        result = ''
        while head is not None:
            result += str(head.val) + '->'
            head = head.next
        print(result)


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    # l3 = ListNode(3)
    # l4 = ListNode(4)
    # l5 = ListNode(5)

    l1.next = l2
    # l2.next = l3
    # l3.next = l4
    # l4.next = l5

    solution = Solution()
    solution.print_list_node(l1)
    # reversed_l1 = solution.swapPairs(l1)
    reversed_l1 = solution.reverseKGroup(l1, 2)
    solution.print_list_node(reversed_l1)
