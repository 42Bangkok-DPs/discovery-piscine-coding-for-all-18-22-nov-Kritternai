def is_valid_position(x, y, size):
    return 0 <= x < size and 0 <= y < size

def parse_board(board):
    """Parse board into a 2D list and find the king's position."""
    lines = board.strip().split('\n')
    size = len(lines)

    # ตรวจสอบว่ากระดานเป็นสี่เหลี่ยมจัตุรัส
    if any(len(line) != size for line in lines):
        return None, None, None

    valid_pieces = {'P', 'B', 'R', 'Q', 'K', '.'}
    for line in lines:
        if any(char not in valid_pieces for char in line):
            return None, None, None

    board_array = [list(line) for line in lines]
    king_pos = None

    king_count = 0
    for y, row in enumerate(board_array):
        for x, cell in enumerate(row):
            if cell == 'K':
                king_pos = (x, y)
                king_count += 1
                if king_count > 1:
                    return None, None, None

    if king_count == 0:
        return None, None, None

    return board_array, king_pos, size

def check_directions(board, king_x, king_y, size, directions, targets):
    """Check if any piece from `targets` attacks the king in `directions`."""
    for dx, dy in directions:
        x, y = king_x + dx, king_y + dy
        while is_valid_position(x, y, size):
            piece = board[y][x]
            if piece in targets:
                return True
            if piece != '.':
                break
            x, y = x + dx, y + dy
    return False

def check_pawn(board, king_x, king_y, size):
    """Check if a pawn attacks the king."""
    return any(
        is_valid_position(king_x + dx, king_y + 1, size) and 
        board[king_y + 1][king_x + dx] == 'P'
        for dx in (-1, 1)
    )

def checkmate(board):
    """Check if the king is in check."""
    try:
        board_array, king_pos, size = parse_board(board)

        # หากกระดานผิดเงื่อนไขใด ๆ ให้ Fail
        if board_array is None or king_pos is None:
            print("Fail")
            return

        king_x, king_y = king_pos

        if (check_pawn(board_array, king_x, king_y, size) or
            check_directions(board_array, king_x, king_y, size, [(1, 1), (1, -1), (-1, 1), (-1, -1)], {'B', 'Q'}) or
            check_directions(board_array, king_x, king_y, size, [(0, 1), (0, -1), (1, 0), (-1, 0)], {'R', 'Q'})):
            print("Success")
        else:
            print("Fail")
    except Exception:
        print("Fail")