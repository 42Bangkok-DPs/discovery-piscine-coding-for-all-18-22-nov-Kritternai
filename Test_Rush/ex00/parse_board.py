def parse_board(board):
    
    # 1. ย้อนกลับไปอ่าน discovery-piscine-coding-for-all-18-22-nov-Kritternai/Test_Rush/ex00/get_board_size.py Line 2
    lines = board.strip().split('\n')
    #lines = ['R...', '.K..', '..P.', '....']
    # 2. ย้อนกลับไปอ่าน discovery-piscine-coding-for-all-18-22-nov-Kritternai/Test_Rush/ex00/get_board_size.py Line 3
    size = len(lines)
    #size = 4
    # 3. สร้าง variable เก็บ log board และ log king
    board_array = []  # board ((((2D list))))
    king_pos = None   # King Position เดี๋ยวใช้สำหรับเก็บ (x, y)

    # 4. loop
    for y, line in enumerate(lines):
        row = []
        for x, char in enumerate(line):
            row.append(char)  # เพิ่ม (Char) ลงในแถว
            if char == 'K':   # find King
                king_pos = (x, y)  # log king
        board_array.append(row)  # add row to board
    #row = ['R', '.', '.', '.']
    #row = ['.', 'K', '.', '.']
    #king_pos = (1, 1)
    #row = ['.', '.', 'P', '.']
    #row = ['.', '.', '.', '.']

    '''board_array = [
    ['R', '.', '.', '.'],
    ['.', 'K', '.', '.'],
    ['.', '.', 'P', '.'],
    ['.', '.', '.', '.']
    ]'''

    # 5. 2D, posi King, sz
    return board_array, king_pos, size
    
    '''board_array = [
    ['R', '.', '.', '.'],
    ['.', 'K', '.', '.'],
    ['.', '.', 'P', '.'],
    ['.', '.', '.', '.']
    ]
    king_pos = (1, 1)  C 1 R 1
    size = 4  4x4'''

board = """\
R...
.K..
..P.
....\
"""

board_array, king_pos, size = parse_board(board)

print(board_array)
# [['R', '.', '.', '.'], ['.', 'K', '.', '.'], ['.', '.', 'P', '.'], ['.', '.', '.', '.']]

print(king_pos)
# (1, 1)
X
print(size)
# 4