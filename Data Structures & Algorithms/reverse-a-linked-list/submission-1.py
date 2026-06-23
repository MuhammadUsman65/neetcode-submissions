class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)

        # on the way BACK, reverse the pointer
        head.next.next = head   # next node points back to current
        head.next = None        # cut current node's forward pointer

        return new_head         # bubble up the new head all the way