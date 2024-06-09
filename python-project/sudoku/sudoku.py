def make_board():
    return [list(map(int, list(input()))) for _ in range(9)]

def print_board(bo):
    for i in range(9):
        if i % 3 == 0 and i != 0:  # 가로 구분선
            print('- ' * 12)

        for j in range(9):
            sep = '  |  ' if j in [2, 5] else ' '  # 세로 구분선
            sep = '\n' if j == 8 else sep  # 줄바꿈
            print(bo[i][j], end = sep)

def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None

def valid(bo, num, pos):
    row, col = pos

    # Check row
    if any(bo[row][i] == num for i in range(9) if i != col):
        return False

    # Check column
    if any(bo[i][col] == num for i in range(9) if i != row):
        return False

    # Check box
    box_x, box_y = col // 3 * 3, row // 3 * 3

    if any(bo[i][j] == num for i in range(box_y, box_y+3) for j in range(box_x, box_x+3) if (i, j) != pos):
        return False

    return True

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    
    row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def main():
    print('스도쿠 문제를 입력해 주세요.')
    print('공백은 0으로 입력')
    board = make_board()
    print("\n해결된 스도쿠 퍼즐:")
    solve(board)
    print_board(board)

if __name__ == "__main__":
    main()
