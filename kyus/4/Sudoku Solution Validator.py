from typing import List


def validate(l: List[int]) -> bool:
    return set(l) == set(range(1, 10))

def check_boxes(board) -> List[int]:
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            square_row = x // 3 * 3
            square_col = y // 3 * 3
            if not validate([
                digit for col in board[square_row:square_row + 3]
                for digit in col[square_col:square_col + 3]
            ]):
                return False
    return True

def valid_solution(board) -> bool:
    return (
        all(map(validate, board))
        and all(map(validate, zip(*board)))
        and check_boxes(board)
    )
