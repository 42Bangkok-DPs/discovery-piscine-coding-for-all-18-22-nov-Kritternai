#!/usr/bin/env python3
import sys
from checkmate import checkmate

def main():
    # Check if at least one file argument is passed
    if len(sys.argv) < 2:
        print("Error")
        return
    
    for filename in sys.argv[1:]:
        try:
            with open(filename, 'r') as file:
                board = file.read().strip()
                checkmate(board)
        except Exception as e:
            print("Error")

if __name__ == "__main__":
    main()