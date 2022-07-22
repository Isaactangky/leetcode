# every time half of the list is drop
# log2 (n) time complexity
# space: O(1)


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid+1
        return -1

            
                
            