'''
Tic-Tac-Toe: Prove
Author: Cristian De La Hoz
'''
def main():

    block = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    gamer = next_gamer("")
    while not (has_winner(block) or is_a_draw(block)):
        create_block(block, gamer)
        gamer = next_gamer(gamer)
    create_block(block, gamer)
    print("Good game. Thanks for playing!")

def create_block(block, gamer):

    print()
    print(f"[{block[0]}][{block[1]}][{block[2]}]")
    print(f"[{block[3]}][{block[4]}][{block[5]}]")
    print(f"[{block[6]}][{block[7]}][{block[8]}]")
    print()

    frame = int(input(f"{gamer}'s to choose a square (1-9):"))
    block[frame - 1] = gamer
    return block

def next_gamer(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

def is_a_draw(block):
    for square in range(9):
        if block[square] != "x" and block[square] != "o":
            return False
    return True 

def has_winner(block):
    return (block[0] == block[1] == block[2] or
            block[3] == block[4] == block[5] or
            block[6] == block[7] == block[8] or
            block[0] == block[3] == block[6] or
            block[1] == block[4] == block[7] or
            block[2] == block[5] == block[8] or
            block[0] == block[4] == block[8] or
            block[2] == block[4] == block[6])

if __name__ == "__main__":
    main()
