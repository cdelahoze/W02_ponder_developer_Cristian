'''
Tic-Tac-Toe: Prove
Author: Cristian De La Hoz
'''

block = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print()

gamer = "x"

while gamer != 10:

    print(f"[{block[0]}][{block[1]}][{block[2]}]")
    print(f"[{block[3]}][{block[4]}][{block[5]}]")
    print(f"[{block[6]}][{block[7]}][{block[8]}]")

    frame = int(input(f"{gamer} to choose a square (1-9):"))
        

    block[frame - 1] = gamer


