"""
https://leetcode.com/problems/sudoku-solver/
"""

import time
from typing import List

check_map = {
    "1": False,
    "2": False,
    "3": False,
    "4": False,
    "5": False,
    "6": False,
    "7": False,
    "8": False,
    "9": False,
}


class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            cm = check_map.copy()
            for val in row:
                if val == ".":
                    continue
                if cm[val]:
                    return False
                cm[val] = True

        # Check columns
        for i in range(len(board[0])):
            cm = check_map.copy()
            for b in board:
                if b[i] == ".":
                    continue
                if cm[b[i]]:
                    return False
                cm[b[i]] = True

        # Check sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                cm = check_map.copy()
                for a in range(i, i + 3):
                    for b in range(j, j + 3):
                        if board[a][b] == ".":
                            continue
                        if cm[board[a][b]]:
                            return False
                        cm[board[a][b]] = True
        return True


class PencilBoard:
    def __init__(self) -> None:
        self.map = {
            "1": False,
            "2": False,
            "3": False,
            "4": False,
            "5": False,
            "6": False,
            "7": False,
            "8": False,
            "9": False,
        }
        self.is_value_provided = False


class Sudoku:
    def __init__(self, board):
        self.board = board
        self.pencil_board = [[PencilBoard() * 9] * 9]

    def is_possible(self, num: str, row_num, col_num) -> bool:
        """We check if a number in certain position is possible or not

        Args:
            num (str): _description_
            row_num (_type_): _description_
            col_num (_type_): _description_

        Returns:
            bool: _description_
        """
        # check row
        row = self.board[row_num]
        for val in row:
            if val == num:
                return False
        # check column
        for b in self.board:
            if b[col_num] == num:
                return False
        # check sub-boxes
        i = (row_num % 3) * 3
        j = (col_num % 3) * 3
        for a in range(i, i + 3):
            for b in range(j, j + 3):
                if board[a][b] == num:
                    return False
        return True

    def init_fast_pencil(self):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    for k, v in self.pencil_board[i][j].map.items():
                        if not v:
                            if self.is_possible(k, i, j):
                                self.pencil_board[i][j].map[k] = True
                else:
                    self.pencil_board[i][j].is_value_provided = True

    def update_fast_pencil(self):
        """Update pencil board based on new value update"""
        pass


nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        all_filled = False
        atleast_one_filled = False
        while (not all_filled or not atleast_one_filled):
            print(board)
            atleast_one_filled = False
            all_filled = True
            for i, row in enumerate(board):
                for j, val in enumerate(row):
                    # print(board[i][j])
                    if board[i][j] == ".":
                        all_filled = False
                        rn = self.checkRow(board, i)
                        cn = self.checkCol(board, j)
                        gn = self.checkGrid(board, i, j)
                        ln = rn.intersection(cn).intersection(gn)
                        if len(ln) == 1:
                            atleast_one_filled = True
                            print(ln)
                            board[i][j] = ln.pop()
            time.sleep(1)

    def checkRow(self, board, rowNum):
        local_nums = nums.copy()
        for n in board[rowNum]:
            if n in local_nums:
                local_nums.remove(n)
        return local_nums

    def checkCol(self, board, colNum):
        local_nums = nums.copy()
        for b in board:
            if b[colNum] in local_nums:
                local_nums.remove(b[colNum])
        return local_nums

    def checkGrid(self, board, rowNum, colNum):
        local_nums = nums.copy()
        grid_row_start = int(rowNum / 3) * 3
        grid_col_start = int(colNum / 3) * 3
        for i in range(grid_row_start, grid_row_start + 3):
            for j in range(grid_col_start, grid_col_start + 3):
                if board[i][j] in local_nums:
                    local_nums.remove(board[i][j])
        return local_nums


def print_sudoku_board(board: List[List[str]]) -> None:
    for b in board:
        print(" ".join(b))


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    board = [
        [".", ".", "9", "7", "4", "8", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "2", ".", "1", ".", "9", ".", ".", "."],
        [".", ".", "7", ".", ".", ".", "2", "4", "."],
        [".", "6", "4", ".", "1", ".", "5", "9", "."],
        [".", "9", "8", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", "8", ".", "3", ".", "2", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "6"],
        [".", ".", ".", "2", "7", "5", "9", ".", "."],
    ]

    Solution().solveSudoku(board=board)
    print_sudoku_board(board)
