from random import randint


def printBoard():
    for i in range(n) :
        for j in range(n) :
            if board[i][j] == pawn:
                print("##", end=" ")
            else:
                print("%02d" % board[i][j], end=" ")
        print("")


n = 8
pawn = 1
a = [[ i*n+j+1 for j in range(n)] for i in range(n)]
board = [ a[i] if i%2==0 else a[i][::-1] for i in range(n)]


print("Starting Game\n\nInitial Board :")
printBoard()

while True:

    print("\n\nPawn Position :", pawn,);
    roll = randint(1,6)
    print("Dice Roll :", roll)
    if pawn+roll <= n*n :
        pawn+=roll
    else:
        print("Invalid Roll")
    printBoard()
        
    ip = input("Continue (y/n) :")
    if ip[0] == 'n':
        break
    else:
        pass

print("GAME OVER")


    

    
    
    


    

    
    
