BOARD = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

def board_print():
    for i in range(-1, len(BOARD)):
        for j in range(-1, len(BOARD)):
            if i == -1 and j == -1:
                print("   ", end="")
            elif i == -1:
                print(f"{j}  ", end="")
            elif j == -1:
                print(f"{i}  ", end="")
            else:
                print(f"{BOARD[i][j]}  ", end="")
        print()

def put_tile(tile):
    j, i = list(
        map(
            int, 
            input("タイルを置く座標を指定してください (x y) > ").split()
        )
    )
    if BOARD[i][j] == "":
        BOARD[i][j] = tile

def is_win(tile):
    for i in range(len(BOARD)):
        if BOARD[i][0] == BOARD[i][1] == BOARD[i][2] == tile:
            print(f"{tile}の勝利")
            return True
        if BOARD[0][i] == BOARD[1][i] == BOARD[2][i] == tile:
            print(f"{tile}の勝利")
            return True
    if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == tile:
        print(f"{tile}の勝利")
        return True
    if BOARD[0][2] == BOARD[1][1] == BOARD[2][0] == tile:
        print(f"{tile}の勝利")
        return True
    return False

while True:
    # 自分のターン
    board_print()
    put_tile("O") # 自分のターンはOを置く
    if is_win("O"):
        break
    # 相手のターン
    board_print()
    put_tile("X") # 相手のターンはXを置く
    if is_win("X"):
        break