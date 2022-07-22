// time: binary search O(logn)
// compare nums[mid] with nums[l]
// 1. if nums[mid] >= nums[l]: if target < nums[l] or target > nums[mid]
// search the right portion, else search the left portion
// 2. if nums[mid] < nums[l]: if target > nums[r] or target < nums[mid]
// search the left portion, else search the right portion

class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l<= r){
            int mid = l + (r - l) / 2;
            //System.out.println(mid);
            if (nums[mid] == target) return mid;
            // left sorted portion
            if (nums[mid] >= nums[l]){
                if (target > nums[mid] || target < nums[l]) l = mid + 1;
                else r = mid  - 1;
            }
            // right sorted portion
            else{
                if (target > nums[r] || target < nums[mid]) r = mid - 1;
                else l = mid + 1;
            }
        }
        return -1;
    }
}