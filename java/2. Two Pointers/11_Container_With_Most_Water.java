// left, right as the two edges
// volum = (right - left) * lower edge
// to search for the thinner containers, we keep the higher edge
// since width is smaller for a thinner container
// its volume > maxVol only when it has a higher min(heights)

// time: O(n) iterate the height array
// space: O(1) 

class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxVol = 0;
        while (left < right){
            int curVol = (right - left) * Math.min(height[left], height[right]);
            maxVol = Math.max(maxVol, curVol);
            if (height[left] <= height[right] ){
                left++;
            }else{
                right--;
            }
        
                
        }
        return maxVol;
        
    }
}