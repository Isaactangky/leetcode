/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) return head;
        ListNode dummy = new ListNode(-1, head);
        ListNode left = dummy, right = dummy;
        while (right != null && n > 0){
            right = right.next;
            n -= 1;
        }
        if (right == null) return head;
        while (right.next != null){
            left = left.next;
            right = right.next;
        }
        // left: node before the node being removed
        ListNode tmp = left.next.next;
        left.next = tmp;
        
        return dummy.next;
    }
}