
"""
338. Counting Bits
0:0
1:1, 2:1, 3:2, 4:1, 5:2, 6:2
if i is even:
res[i] = res[i//2] 
i is odd:
res[i] = res[i//2]+ 1

4:100  // 2  -> 2:10 num of 1 bits unchanged
5:101  // 2  -> 2:10 we dropped A 1 bit

"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        res =   [0]
        for i in range(1, n + 1):
            bits = res[i//2] + i % 2
            res.append(bits)
        return res
        