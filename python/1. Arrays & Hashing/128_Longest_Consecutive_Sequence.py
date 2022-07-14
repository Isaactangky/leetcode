
"""
Created on Thu Jul 14 14:44:26 2022

@author: IsaacTang
"""
#method one, removing left and right and increase length
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            #check if it is in the set
            #since some ele remove previously, the check is reduced
            if n  in numSet:
                #check both left and right 
                #if exist, remove from the set
                #and check further left and right
                left = n - 1
                right = n + 1
                while left in numSet: 
                    numSet.remove(left)
                    left -= 1
                while right in numSet:
                    numSet.remove(right)
                    right += 1
                longest = max( longest, right - left - 1)
                numSet.remove(n)
                #when len(numSet) <= longest, 
                #impossible to construct an subarray longer than longest
                if len(numSet) <= longest:
                    return longest
                
        return longest

# Method 2: only check num at the start of sequece
# time: O(n) iterate nums 
# space: O(n) for set storage
class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            # only check the start
            if n - 1 not in numSet:

                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max( longest, length)
                

        return longest