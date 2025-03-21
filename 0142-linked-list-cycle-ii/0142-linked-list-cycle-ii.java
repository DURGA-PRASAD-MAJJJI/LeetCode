public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) return null;

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null &&fast.next.next!=null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                int r = fast.next.val;
                ListNode temp = head;
                int c = 0;
                while (temp != slow) {
                    temp=temp.next;
                    slow=slow.next;
                    c++;
                }
                return temp;
            }
        }  return null;     
    }   
}
