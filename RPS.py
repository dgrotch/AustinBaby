
def rpc():
    y = True
    while y:
        i = input("Player 1: R/P/S? ")
        j = input("Player 2: R/P/S? ")

        if i == 'R' and j == 'P':
            print("Paper beats rock, P2 wins!")
        elif i == 'P' and j == 'R':
            print("Paper beats rock, P2 wins!")
        elif i == 'S' and j == 'R':
            print("Rock beats scissors, P1 wins!")
        elif i == 'R' and j == 'S':
            print("Rock beats scissors, P2 wins!")
        elif i == 'P' and j == 'S':
            print("Scissors beats paper, P2 wins!")
        elif i == 'S' and j == 'P':
            print("Scissors beats paper, P1 wins!")
        else: 
            print("Same choice, play again")
            continue

        a = input("keep playing? ")
        if a == 'n':
            y = False

if __name__ == '__main__':
    rpc()


