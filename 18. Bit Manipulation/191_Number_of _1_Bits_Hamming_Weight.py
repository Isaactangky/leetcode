
"""
191. Number of 1 Bits
check if the last bit is 1 -> change count
drop last bit 
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += (n & 1)
            n >>= 1
        return count
"""
n & n - 1: removing a 1 bit
"""   
class Solution2:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count