#!/usr/bin/env python3 
def main():
    board = """\
R...
.K..
..P.
.L.k\
"""
    rows = board.split()
    print(len(rows))
    for x in rows:
        print(x)
    # for i in range(0,len(rows)+1):
    #     print(board.split()[i][i])
main()
    