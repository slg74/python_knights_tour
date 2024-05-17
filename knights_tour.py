from typing import List

N = 8  # 8x8 chessboard


# walk_board - walk a Knight chess piece on a solved knight's tour of an N x N chessboard.
def walk_board(
    x: int, y: int, m: int, board: List[List[int]], xmoves: List[int], ymoves: List[int]
) -> bool:
    if m == N * N:
        print_board(board)
        return True

    for i in range(N):
        next_x = x + xmoves[i]
        next_y = y + ymoves[i]
        if can_move(next_x, next_y, board):
            board[next_x][next_y] = m
            if walk_board(next_x, next_y, m + 1, board, xmoves, ymoves):
                return True
            else:
                board[next_x][next_y] = -1

    return False


def can_move(x: int, y: int, board: List[List[int]]) -> bool:
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1


# Print a solved NxN chessboard.
def print_board(board):
    for i in range(N):
        for j in range(N):
            if i % 2 == j % 2:
                print(
                    # Ansi reverse video for white squares.
                    f"\u001b[7m{board[i][j]:3}\u001b[0m",
                    end="",
                )
            else:
                print(
                    # Ansi sane video for black squares.
                    f"{board[i][j]:3}",
                    end="",
                )
        print()


def main():
    # chessboard of NxN squares
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # all potential x and y moves
    xmoves = [2, 1, -1, -2, -2, -1, 1, 2]
    ymoves = [1, 2, 2, 1, -1, -2, -2, -1]

    # Mark the starting square, 0,0 as value 0.
    board[0][0] = 0

    if not walk_board(0, 0, 1, board, xmoves, ymoves):
        print("No solution.")
        return


if __name__ == "__main__":
    main()
