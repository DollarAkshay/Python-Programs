import copy

def winner(m):
    #rows 
    for i in range(0,3):
        if m[i][0]==m[i][1] and m[i][0]==m[i][2]:
            if m[i][0]!=0:
                return m[i][0]
    #cols
    for i in range(0,3):
        if m[0][i]==m[1][i] and m[0][i]==m[2][i]:
            if m[0][i]!=0:
                return m[0][i]
    #diagonal right
    if m[0][0]==m[1][1] and m[0][0]==m[2][2]:
        if m[0][0]!=0:
            return m[0][0]
    #diagonal left
    if m[0][2]==m[1][1] and m[0][2]==m[2][0]:
        if m[0][2]!=0:
            return m[0][2]
    #return -1 if the game is still not over
    for i in range(0,3):
        for j in range(0,3):
            if m[i][j]==0:
                return -1
    #tie
    return 0

#finds out possible moves
def possible_moves(m):
    lst=[]
    for i in range(0,3):
        for j in range(0,3):
            if m[i][j]==0:
                lst.append((i,j))
    return lst

def tic_tac_toe(m,r,c,computer,no_of_moves=0):
    if computer: #initial value of computer = False
        m[r][c]=2 #2 is for human player
    else: 
        m[r][c]=1 #1 is for computer
    computer=not computer

    score = winner(m)
    if score==1:
        return 10-no_of_moves
    elif score==2:
        return no_of_moves-10
    elif score==0:
        return 0

    moves = possible_moves(m)
    score_lst = []
    for i in moves:
        m2 = copy.deepcopy(m)
        score_lst.append(tic_tac_toe(m2, i[0], i[1], computer,no_of_moves+1))

    if computer:
        return max(score_lst)
    if not computer:
        return min(score_lst)


#game play


def game_play():
    m=[[2, 1, 1],
       [0, 2, 2],
       [0, 0, 1]]
    while True:
        moves = possible_moves(m)
        #computer's move
        score_lst2=[]
        m2=copy.deepcopy(m)
        for i in moves:
            score_lst2.append(tic_tac_toe(m2, i[0], i[1], computer=False))
        max_move_index = score_lst2.index(max(score_lst2))
        move = moves[max_move_index]
        m[move[0]][move[1]]=1
        print(m)
        if winner(m)==1:
            print("computer wins")
            break
        elif winner(m)==0:
            print("tie")
            break
        #human move
        r,c = map(int,input("enter row and col: ").split())
        m[r][c]=2
        print(m)
        if winner(m)==2:
            print("human wins")
            break
        elif winner(m)==0:
            print("tie")
            break
game_play()