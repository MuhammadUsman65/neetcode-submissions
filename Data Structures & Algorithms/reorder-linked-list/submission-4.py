# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        #finding middle point, slow.next after the loop will be the breaking point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        #will be the last node while merging so setting it to null
        slow.next = None

        #reversing the second half
        prev = None
        while second_half:
            curr_next = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = curr_next

        #merge the two halves
        second = prev
        first = head

        while second:
            tmp1=first.next
            tmp2 = second.next
            first.next = second
            second.next =tmp1
            first = tmp1
            second = tmp2

        
        