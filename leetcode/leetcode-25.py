# Question: Reverse Nodes in k-Group
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in the
# end should remain as it is.

# Example:
# Given 1->2->3->4->5.
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5

# Note:
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself
# may be changed.


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        # check if head is NULL List
        if head is None or head.next is None:
            return head

        # get the number of nodes
        list_length = 0
        new_head = head
        while new_head is not None:
            list_length += 1
            new_head = new_head.next

        # If the length of nodes is less than the number of group
        if list_length < k:
            return head

        # calculate the number of groups that can be reversed
        number_of_groups = int(list_length / k)

        return self.swapPairs(head, k, number_of_groups)

    def swapPairs(self, head: ListNode, k, number_of_groups, number_of_reversed_groups=0) -> ListNode:

        prev = None
        current = head
        n = k

        # reverse the node due to the count of n
        # After the reversal is completed，
        # prev is the new head of the group that has been reversed.
        # current points the head of the next group to be processed.
        # head is the new end of the group that has been reversed.
        while current and n > 0:
            n -= 1
            next = current.next
            current.next = prev
            prev = current
            current = next

        # after a group of nodes is reversed, then increase 1.
        number_of_reversed_groups += 1

        # determine whether to reverse the next group
        if current is not None and number_of_reversed_groups < number_of_groups:
            head.next = self.swapPairs(
                current, k, number_of_groups, number_of_reversed_groups)
        else:
            head.next = current
        return prev

    def print_list_node(self, head: ListNode):
        result = ''
        while head is not None:
            result += str(head.val) + '->'
            head = head.next
        print(result.rstrip('->'))


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    solution = Solution()
    solution.print_list_node(l1)
    reversed_l1 = solution.reverseKGroup(l1, 2)
    solution.print_list_node(reversed_l1)
