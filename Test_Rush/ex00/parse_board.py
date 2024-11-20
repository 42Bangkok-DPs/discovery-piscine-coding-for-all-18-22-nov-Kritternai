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
    for y, line in enumerate(lines):  # y คือดัชนีของแถว
        row = []  # ใช้เก็บข้อมูลของแต่ละแถว
        for x, char in enumerate(line):  # x คือดัชนีของแต่ละคอลัมน์
            row.append(char)  # เพิ่มตัวอักษร (หมาก) ลงในแถว
            if char == 'K':   # ถ้าพบ King (K)
                king_pos = (x, y)  # บันทึกตำแหน่ง (x, y)
        board_array.append(row)  # เพิ่มแถวนี้ลงในกระดาน



    # 5. 2D, posi King, sz
    return board_array, king_pos, size

board = """\
R...
.K..
..P.
....\
"""