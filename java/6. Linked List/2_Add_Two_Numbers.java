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
// carry to record carry value to the next digit
// current digit val = (list1.val + list2.val + carry) % carry
// update carry to carry / 10
// time: O(max(m, n)) m, n for length of the linked lists
// space: O(max(m, n))

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy_head = new ListNode(-1);
        ListNode p = dummy_head;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0){
            if (l1 != null){
                carry += l1.val;
                l1 = l1.next;
            }
            if (l2 != null){
                carry += l2.val;
                l2 = l2.next;
            }
            p.next = new ListNode(carry % 10);
            p = p.next;
            carry = carry / 10;
        }
        return dummy_head.next;
    }
}