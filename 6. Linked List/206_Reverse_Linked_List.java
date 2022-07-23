/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 * temp to hold nodes after head
 * place the head to the front of previous nodes
 * time: O(n)
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        
        ListNode pre = null;
        while (head != null){
            ListNode temp = head.next;
            head.next = pre;
            pre = head;
            head = temp;
        }
        return pre;
    }
}