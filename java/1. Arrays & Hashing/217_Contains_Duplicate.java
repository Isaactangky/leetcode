class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet <Integer> HashSet = new HashSet();
        for (int i = 0; i< nums.length; i++){
            if (HashSet.contains(nums[i])) {
                return true;
            }
            else {
                HashSet.add(nums[i]);
                
            }
        
        }
        return false;
    }
}
