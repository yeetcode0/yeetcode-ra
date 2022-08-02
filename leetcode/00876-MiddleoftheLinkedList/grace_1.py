class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            append_val = head
            arr.append(append_val)
            head = head.next
        middle_index = len(arr) // 2
        return arr[middle_index]
