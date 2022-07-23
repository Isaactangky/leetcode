"""
XOR logic:
num ^ num = 0
 0 ^ num = num
 """
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        for i in range( len(nums)):
            res ^= nums[i]
            #print(res)
        return res
