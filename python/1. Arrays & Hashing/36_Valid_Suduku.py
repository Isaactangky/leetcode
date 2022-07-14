
"""
3 dicts of set for row, col and box
box key is (i//3, j//3)
time: O(rows * cols)
space:  O(rows * cols) dicts could store rows * cols vals
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        row_dict = collections.defaultdict(set)
        col_dict = collections.defaultdict(set)
        box_dict = collections.defaultdict(set)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] != '.':
                    val = board[i][j]
                    if (val in row_dict[i] or val in col_dict[j] or
                        val in box_dict[(i//3, j//3)]):
                        return False
                    row_dict[i].add(val)
                    col_dict[j].add(val)
                    box_dict[(i//3, j//3)].add(val)
        return True