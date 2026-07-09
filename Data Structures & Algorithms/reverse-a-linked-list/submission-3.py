class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None   # will become the new head
        curr = head   

        while curr:
            next_node = curr.next
            curr.next = prev       
            prev = curr
            curr = next_node       # move curr forward to the node saved earlier

        return prev  # prev ends up at the new head once curr runs off the end