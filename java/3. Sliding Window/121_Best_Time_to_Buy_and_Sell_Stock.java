class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        int left = 0, right = 0;
        while (right < prices.length){
            if (prices[right] > prices[left]){
                res = Math.max(res, prices[right] - prices[left]);
            }
            if (prices[right] < prices[left]){
                left = right;
                
            }
            right++;
        }
        return res;
    }
}