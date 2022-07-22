# binary search the possible values of k (1, max(piles))
# hours needed for each pile is ceiling of (pile / k)
# l pointer will be the minimum val of k
# log2 (n) time complexity
# space: O(1)


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1 , max(piles)
        
        while l <= r:
            m = l + (r - l) //2
            minH = 0
            for c in piles:
                minH += math.ceil(c/m)
            
            if minH > h:
                l = m + 1
            else:
                r = m - 1
        return l
        
                
        

            
                
            