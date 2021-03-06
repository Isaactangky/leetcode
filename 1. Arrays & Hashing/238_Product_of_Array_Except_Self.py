
"""
[1 2 3 4]
res for 2: pre (1) * post (3 * 4)
time: O(2n) = O(n)
space: O(n) for res
 
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res