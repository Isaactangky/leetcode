class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        HashMap <Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
            int another = target - nums[i];
            if (map.containsKey(another)){
                res[0] = map.get(another);
                res[1] = i;
                break;
            }
            else{
                map.put(nums[i], i);
            }
        }
        return res;
    }
}
