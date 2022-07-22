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

// space: O(1)
// first run fast-slow pointers to prove cycle existence
// then slow reset to head
// move slow and fast one step forward until they meet
// slow or fast will be the node where the cycle begins
// time: O(k + nc + k) where k + nc is the num of nodes from head when fast and slow meet
// 		   k is the length before pos, c is the priemeter of the cycle 
//		   the second k is the num of nodes slow travels to the beginning of the cycle
//

public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null){
            slow = slow.next;
            fast = fast.next;
            if (fast != null){
                fast = fast.next;
            }
            if (slow == fast) break;
        }
        if (fast == null) return null;
        slow = head;
        while (slow != fast){
            slow = slow.next;
            fast = fast.next;
        }
        return fast;
    }
}