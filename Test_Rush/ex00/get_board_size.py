def get_board_size(board):
    #แยกจำนวนบรรทัด Strip ก่อนกัน error split เพื่อทำเป็น list แล้ว len เพื่อเช็ค list
    lines = board.strip().split('\n') 
    #['R...', '.K..', '..P.', '....']
    return len(lines)  
    
board = """\
R...
.K..
..P.
....\
"""

print(get_board_size(board))  #4