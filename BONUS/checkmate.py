#!/bin/env python3
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

# สร้างกระดานหมากรุกด้วย numpy arrays
board = np.array([
    pieces, empty_row, empty_row, empty_row, empty_row, empty_row, empty_row ,pieces2
])
print(board)

def is_valid_move(board, start_pos, end_pos):

    # ตรวจสอบว่าการเคลื่อนไหวนั้นอยู่ภายในกระดานหรือไม่
    if not (0 <= end_pos[0] < 8 and 0 <= end_pos[1] < 8):
        return False

    # ตรวจสอบว่าไม่ได้ย้ายไปยังตำแหน่งเดิม
    if start_pos == end_pos:
        return False

    # เขียนส่วนตรวจสอบเงื่อนไขการเคลื่อนไหวของแต่ละชิ้นหมากรุกที่นี่

    # ตรวจสอบว่ามีชิ้นหมากรุกของฝ่ายตรงข้ามอยู่ที่ตำแหน่งปลายทางหรือไม่
    piece = board[start_pos[0]][start_pos[1]]
    target = board[end_pos[0]][end_pos[1]]
    if target != "." and target.isupper() == piece.isupper():
        return False
    return True
    # print(board)

# สมมติว่าเรากำลังย้ายม้าจาก (0,1) ไป (2,2)
print(is_valid_move(board, (0,1), (2,2)))

def move_piece(board, start_pos, end_pos):
    if is_valid_move(board, start_pos, end_pos):
        board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
        board[start_pos[0]][start_pos[1]] = "."
        print("เคลื่อนไหวสำเร็จ")
    else:
        print("เคลื่อนไหวไม่ถูกต้อง")

# def cheakmate_pawn():
#     if 
    
# def cheakmate():
    #pawn 


def walk():
    global Py1, Px1,Rx1,Ry1,By1,Bx1,Qx1,Qy1
    mate = (str(input("Choose a mate that you want to move >> ")))
    if mate == "P":
        Pey = (int(input("Enter you destination of y >> ")))
        Pex = (int(input("Enter you destination of x >> ")))
        if (Pey == Py1+1) and (Pex == Px1-1 or Pex == Px1+1):
           move_piece(board, P, (Pey,Pex))
           print(is_valid_move(board,(Py1,Px1),(Pey,Pex)))
           print(board)
           Px1=Pex
           Py1=Pey
        else:
            print("NOOB!!")

    elif mate == "R":
        Rey = (int(input("Enter you destination of y >> ")))
        Rex = (int(input("Enter you destination of x >> ")))
        if (Rey == Ry1) and (0 <= Rex < 8):
           move_piece(board, R, (Rey,Rex))
           print(is_valid_move(board,(Ry1,Rx1),(Rey,Rex)))
           print(board)
        elif (Rex == Rx1) and (0 <= Rey < 8):
           move_piece(board, R, (Rey,Rex))
           print(is_valid_move(board,(Ry1,Rx1),(Rey,Rex)))
           print(board)
        else:
            print("NOOB!!")
        Rx1=Rex
        Ry1=Rey

    elif mate == "B":
        Bey = (int(input("Enter you destination of y >> ")))
        Bex = (int(input("Enter you destination of x >> ")))
        if (Bex - Bx1) != 0 and((Bey-By1)/(Bex-Bx1)==1) or ((Bey-By1)/(Bex-Bx1)==-1):
           move_piece(board, B, (Bey,Bex))
           print(is_valid_move(board,(By1,Bx1),(Bey,Bex)))
           print(board)
        else:
            print("NOOB!!")
        Bx1=Bex
        By1=Bey

    elif mate == "Q":
        Qey = (int(input("Enter you destination of y >> ")))
        Qex = (int(input("Enter you destination of x >> ")))
        if (Qey == Qy1) and (0 <= Qex < 8):
           move_piece(board, Q, (Qey,Qex))
           print(board)
        elif (Qex == Qx1) and (0 <= Qey < 8):
           move_piece(board, Q, (Qey,Qex))
           print(board)
        elif (Qex - Qx1) != 0 and ((Qey - Qy1) / (Qex - Qx1) == 1 or (Qey - Qy1) / (Qex - Qx1) == -1):
           move_piece(board, Q, (Qey,Qex))
           print(board)
        else:
            print("NOOB!!")
        print(is_valid_move(board,(Qy1,Qx1),(Qey,Qex)))
        Qx1=Qex
        Qy1=Qey
    else:
        print("Error")
    
def check_mate():
    global Py1, Px1,Rx1,Ry1,By1,Bx1,Qx1,Qy1,Kx,Ky

    if (Ky == Py1+1) and (Kx == Px1-1 or Kx == Px1+1):
        print("Success")
    elif (Ky == Ry1) and (0 <= Kx < 8):
        print("Success")
    elif (Kx == Rx1) and (0 <= Ky < 8):
        print("Success")
    elif (Kx - Bx1) != 0 and((Ky-By1)/(Kx-Bx1)==1) or ((Ky-By1)/(Kx-Bx1)==-1):
        print("Success")
    elif (Ky == Qy1) and (0 <= Kx < 8):
        print("Success")
    elif (Kx == Qx1) and (0 <= Ky < 8):
        print("Success")
    elif (Kx - Qx1) != 0 and ((Ky - Qy1) / (Kx - Qx1) == 1 or (Ky - Qy1) / (Kx - Qx1) == -1):
        print("Success")
    else:
        print("Fail")
        print("Now is King's turn !!!")
        Key = (int(input("Enter you destination of y >> ")))
        Kex = (int(input("Enter you destination of x >> ")))
        if (((Key == Ky)and((Kex == Kx+1)or(Kex == Kx-1)))or((Key == Ky-1)or((Kex == Kx+1)or(Kex == Kx-1)))or((Key == Ky+1)or((Kex == Kx+1)or(Kex == Kx-1)))):
          move_piece(board,(Ky,Kx),(Key,Kex))
          print(is_valid_move(board,(Ky,Kx),(Key,Kex)))
          print(board)
          Ky=Key
          Kx=Kex
          check_mate()
        else :
            print("Error")

def Play():
    walk()
    check_mate()

        
Play()