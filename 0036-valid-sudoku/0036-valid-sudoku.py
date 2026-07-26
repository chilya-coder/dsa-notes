from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # dicts for col, row and sub-boxes uniqueness
        # idx_col -> set()
        # idx_row -> set()
        # (idx_box_col, idx_box,row) -> set()

        # // 3 groups adjacent indices together

        col = defaultdict(set)
        row = defaultdict(set)
        boxes = defaultdict(set)

        for idx_r, board_row in enumerate(board):
            for idx_c, val in enumerate(board_row):
                if val == '.': continue
                if val in col[idx_c] or val in row[idx_r] or val in boxes[(idx_r // 3, idx_c // 3)]:
        # dicts for col, row and sub-boxes uniqueness
        # idx_col -> set()
        # idx_row -> set()
        # (idx_box_col, idx_box,row) -> set()

        # // 3 groups adjacent indices together

        col = defaultdict(set)
        row = defaultdict(set)
        boxes = defaultdict(set)

        for idx_r, board_row in enumerate(board):
            for idx_c, val in enumerate(board_row):
                if val == '.': continue
                if val in col[idx_c] or val in row[idx_r] or val in boxes[(idx_r // 3, idx_c // 3)]:
                    return False
                else:
                   col[idx_c].add(val)
                   row[idx_r].add(val) 
                   boxes[(idx_r // 3, idx_c // 3)].add(val)
                   col[idx_c].add(val)
                   row[idx_r].add(val) 
                   boxes[(idx_r // 3, idx_c // 3)].add(val)
        return True

def main():
    test_board = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    solution = Solution()
    result = solution.isValidSudoku(test_board)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()