#!/usr/bin/env python3
# main.py
from checkmate import checkmate

def main():
    test_cases = [
        # 1. Valid Rook attack
        """\
R...
.K..
....
....\
""",
        # 2. Valid Bishop attack
        """\
B...
.K..
....
....\
""",
        # 3. Invalid board (non-square)
        """\
R...
.K.\
""",
        # 4. Invalid characters
        """\
R..X
.K..
....
....\
""",
        # 5. King safe (no threats)
        """\
....
.K..
....
....\
""",
        # 6. Two Kings (invalid)
        """\
K...
.K..
....
....\
""",
        # 7. King at edge attacked by Rook
        """\
....
....
....
R..K\
""",
        # 8. Queen attacking King diagonally
        """\
....
.K..
...Q
....\
""",
        # 9. King surrounded by friendly pieces
        """\
....
.PP.
PKP.
.PP.\
"""
    ]
    
    for idx, board in enumerate(test_cases, 1):
        checkmate(board)

if __name__ == "__main__":
    main()