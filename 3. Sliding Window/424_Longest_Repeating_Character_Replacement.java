class Solution {
    public int characterReplacement(String s, int k) {
        // record maxFre of the chars
        // the max window size is maxFre + k
        // when current string size > maxFre + k, drop left (and reduce its freq)
        // time: O(n) iterate the string once only
        // space: O(n) hashmap could have n keys
        
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int left = 0, right = 0;
        int maxFre = 0;
        int res = 0;
        while (right < s.length()){
            
            map.put(s.charAt(right), map.getOrDefault(s.charAt(right), 0) + 1);
            maxFre = Math.max(maxFre, map.get(s.charAt(right)));
            
            while (right - left - maxFre + 1> k){
                map.put(s.charAt(left), map.get(s.charAt(left) ) - 1);
                left++;
            }
            
            res = Math.max(res, right - left + 1);
            right++;
        }
        return res;
    }
}