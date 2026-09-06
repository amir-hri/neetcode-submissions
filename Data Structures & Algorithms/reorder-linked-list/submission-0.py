# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        size=0
        ll=head
        while ll:
            size+=1
            ll=ll.next
        mid = (size+1)//2
        curr = head
        for _ in range(mid-1):
            curr = curr.next
        second_half = curr.next
        curr.next = None
        first_half = head
        curr = second_half
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_half = prev
        while second_half:
            fh = first_half.next
            sh = second_half.next

            first_half.next = second_half
            second_half.next = fh

            first_half = fh
            second_half = sh


        