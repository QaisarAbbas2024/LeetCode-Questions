# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []

        # Step 1: Extract all node values from each list
        for l in lists:
            while l:
                values.append(l.val)
                l = l.next

        # Step 2: Sort all values
        values.sort()

        # Step 3: Build a new sorted linked list
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next