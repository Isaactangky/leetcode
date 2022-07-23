# Method 1: treat it as 1D array
# row = mid // cols and col = mid % cols
# O(log2 (m * n)) time complexity
# space: O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,  COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            val = matrix[m // COLS][ m % COLS]
            if val == target:
                return True
            elif val < target:
                l = m + 1
            else:
                r = m - 1
        return False

# Method 2: search at the last num of a row
# increase row until the num is greater than target
# then decrease col to search the row
# time: O(m + n) for the worse case, we go through the rows (m nums)
#	and iterate entire last row (n nums)
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
	rl, cl = len(matrix), len(matrix[0])
        row, col = 0, cl -1
        while (row < rl and col > -1):
            val = matrix[row][col]
            if val == target:
                return True
            if val < target:
                row += 1
            else:
                col -= 1
        return False
            
                
            