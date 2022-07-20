/*
 * split LL into 2 LLs O(n)
 * reverse the second LL O(n)
 * merget the LLs O(n)
 * time: O(n)
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
    public void reorderList(ListNode head) {
        if (head.next == null) return;
        ListNode p1 = head, p2 = head.next;
        while (p2.next != null){
            p1 = p1.next;
            p2 = p2.next;
            if (p2.next != null) p2 = p2.next;
        }
        //p1: last of first LL
        ListNode second_head = p1.next;
        p1.next = null;
    
        ListNode list1 = head, list2 =  reverse(second_head);
        head = merge(list1, list2);
        
    }
    

    
    public ListNode reverse(ListNode head){
        ListNode pre = null;
        while (head != null){
            ListNode temp = head.next;
            head.next = pre;
            pre = head;
            head = temp;
        }
        return pre;
        
    }
    public ListNode merge(ListNode list1, ListNode list2){
        ListNode dummy = new ListNode(-1);
        ListNode p = dummy;
        while (list1 != null || list2 != null){
            if (list1 != null){
                p.next = list1;
                list1 = list1.next;
                p = p.next;
            }
            if (list2 != null){
                p.next = list2;
                list2 = list2.next;
                p = p.next;
            }
        }
        return dummy.next;
    }

}