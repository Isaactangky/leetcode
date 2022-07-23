/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
// Floyd's cycle-finding algorithm, also know as tortoise and hare algorithm
// two references to the list and move them at different speeds. 
// Move one forward by 1 node and the other by 2 nodes. 
// If the linked list has a loop they will definitely meet
// time: O(k + nc) where k + nc is the num of nodes from head when fast and slow meet
// 		   k is the length before pos, c is the priemeter of the cycle
// space: O(1)

public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        //if (head.next == null) return false;
        ListNode slow = head, fast = head.next;
        while (fast != null){
            slow = slow.next;
            fast = fast.next;
            if (fast != null){
                fast = fast.next;
            }
            if (slow == fast){
                return true;
            }
        }
        return false;
    }
}