class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = second = head
        while second and second.next:
            first = first.next
            second = second.next.next
        return first
