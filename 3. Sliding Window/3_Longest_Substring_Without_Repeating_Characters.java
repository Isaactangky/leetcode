class Solution {
    public int lengthOfLongestSubstring(String s) {
        // sliding window - if the set contains s[right], 
        // shift the left until s[right] is not in set 
        // -> a new window
        // time: O(s.length()) - iterate the string once only
        // space: O(s.length()) - the set could contains s.length() nunber of char 
        HashSet<Character> charSet = new HashSet<Character>();
        int res = 0;
        int left = 0, right = 0;
        while (right < s.length()){
            
            while (charSet.contains(s.charAt(right))){
                //System.out.println(s.charAt(right) + " " + s.charAt(left));
                res = Math.max(right - left, res);
                charSet.remove(s.charAt(left));
                left++;    
            }
            charSet.add(s.charAt(right));
            right++;
        }
        //System.out.println(right + " " +left);
        res = Math.max(right - left, res);
        return res;
        
    }
}