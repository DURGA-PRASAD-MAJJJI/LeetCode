class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel=ListNode(0, head)
        connector, walker=sentinel, head
        while walker and walker.next:
            next_start=walker.next.next
            temp=walker.next
            temp.next=walker
            walker.next=next_start
            connector.next=temp
            connector=walker
            walker=next_start
        return sentinel.next
        