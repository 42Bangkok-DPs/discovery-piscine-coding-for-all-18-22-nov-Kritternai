def is_in_bounds(r, c, rows, cols):
    """ตรวจสอบว่าตำแหน่ง (r, c) อยู่ในขอบเขตของกระดานหรือไม่"""
    return 0 <= r < rows and 0 <= c < cols

def print_board(board, piece_name=""):
    """พิมพ์กระดานหมากรุก"""
    print(f"{piece_name} Movement Pattern (x = possible moves, o = piece position):")
    for row in board:
        print(" ".join(row))
    print()

def simulate_pawn_attack(board, r, c):
    """จำลองการโจมตีของ Pawn (เบี้ย)"""
    rows, cols = len(board), len(board[0])
    for dr, dc in [(-1, -1), (-1, 1)]:  # โจมตีทแยงมุมซ้ายและขวาบน
        nr, nc = r + dr, c + dc
        if is_in_bounds(nr, nc, rows, cols):
            board[nr][nc] = 'x'
    board[r][c] = 'o'  # แสดงตำแหน่งของตัวหมาก

def simulate_bishop_attack(board, r, c):
    """จำลองการโจมตีของ Bishop (ทหารม้า)"""
    rows, cols = len(board), len(board[0])
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # ทิศทางทแยงมุมทั้ง 4 ทิศ
    for dr, dc in directions:
        nr, nc = r, c
        while True:
            nr += dr
            nc += dc
            if not is_in_bounds(nr, nc, rows, cols):
                break
            board[nr][nc] = 'x'
    board[r][c] = 'o'  # แสดงตำแหน่งของตัวหมาก

def simulate_rook_attack(board, r, c):
    """จำลองการโจมตีของ Rook (เรือ)"""
    rows, cols = len(board), len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # ทิศทางตรงแนวนอนและแนวตั้ง
    for dr, dc in directions:
        nr, nc = r, c
        while True:
            nr += dr
            nc += dc
            if not is_in_bounds(nr, nc, rows, cols):
                break
            board[nr][nc] = 'x'
    board[r][c] = 'o'  # แสดงตำแหน่งของตัวหมาก

def simulate_queen_attack(board, r, c):
    """จำลองการโจมตีของ Queen (ราชินี)"""
    rows, cols = len(board), len(board[0])
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]  # ทั้ง 8 ทิศทาง
    for dr, dc in directions:
        nr, nc = r, c
        while True:
            nr += dr
            nc += dc
            if not is_in_bounds(nr, nc, rows, cols):
                break
            board[nr][nc] = 'x'
    board[r][c] = 'o'  # แสดงตำแหน่งของตัวหมาก

def check_attack_success(board):
    """ตรวจสอบว่าเรามีการโจมตีสำเร็จหรือไม่ (ดูว่ามีการใส่ 'x' ในกระดานหรือไม่)"""
    for row in board:
        if 'x' in row:  # ถ้ามีตำแหน่งที่มี 'x' แสดงว่าโจมตีสำเร็จ
            return True
    return False

def main():
    """ฟังก์ชันหลักเพื่อจำลองการโจมตีของชิ้นส่วนหมากรุก"""
    # สร้างกระดานหมากรุกขนาด 8x8 ที่ว่างเปล่า
    board = [['.' for _ in range(8)] for _ in range(8)]
    
    # จำลองการโจมตีของแต่ละชิ้นส่วนหมากรุก
    # Pawn ที่ตำแหน่ง (3, 3)
    board_pawn = [row[:] for row in board]
    simulate_pawn_attack(board_pawn, 3, 3)
    print_board(board_pawn, "Pawn (P)")

    # Bishop ที่ตำแหน่ง (3, 3)
    board_bishop = [row[:] for row in board]
    simulate_bishop_attack(board_bishop, 3, 3)
    print_board(board_bishop, "Bishop (B)")

    # Rook ที่ตำแหน่ง (3, 3)
    board_rook = [row[:] for row in board]
    simulate_rook_attack(board_rook, 3, 3)
    print_board(board_rook, "Rook (R)")

    # Queen ที่ตำแหน่ง (3, 3)
    board_queen = [row[:] for row in board]
    simulate_queen_attack(board_queen, 3, 3)
    print_board(board_queen, "Queen (Q)")

if __name__ == "__main__":
    main()