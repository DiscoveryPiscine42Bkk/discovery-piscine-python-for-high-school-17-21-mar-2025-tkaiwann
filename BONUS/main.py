from checkmate import check_mate
from checkmate import walk
from checkmate import move_piece
from checkmate import is_valid_move

import numpy as np

# ตั้งค่าคอนฟิกชิ้นหมากรุกและม้วนหมากรุก
pieces = [".", "P", ".", "Q", ".", "B", ".", "R"]
pieces2 = [".", ".", ".", ".", "K", ".", ".", "."]
empty_row = ["."] * 8

# ตัวแปร
Py1=0 
Px1=1 

Ry1=0
Rx1=7 

By1=0 
Bx1=5 

Qy1=0
Qx1=3

Kx=4
Ky=7

P = (Py1,Px1)
R = (Ry1,Rx1)
B = (By1,Bx1)
Q = (Qy1,Qx1)
K = (Kx,Ky)
board = np.array([
    pieces, empty_row, empty_row, empty_row, empty_row, empty_row, empty_row ,pieces2
])
print(board)

def Play():
    walk()
    check_mate()

        
Play()