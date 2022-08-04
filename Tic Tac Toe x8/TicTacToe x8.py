import random
GameRunning=False
Winner=None
CurrentUser="X"
Board=["-","-","-","-","-","-","-","-",
       "-","-","-","-","-","-","-","-",
       "-","-","-","-","-","-","-","-",
       "-","-","-","-","-","-","-","-",
       "-","-","-","-","-","-","-","-",
       "-","-","-","-","-","-","-","-",
       "-","-","-","-","-","-","-","-",
       "-","-","-","-","-","-","-","-",]
def PrintingBoard(Board):
    first=0
    last=8
    for i in range(0,8):
        if(i>=1):
            print("-------------------------------")
        for j in range(first,last):
            print(Board[j]+" | ", end=(""))
        print()
        first=last
        last=last+8
        

def inputFromUser(Board):
    number=int(input("Please enter a number from 1 till 64: "))
    while(number<1 or number>64 or Board[number-1]!="-"):
        print("The number enterd is taken")
        number=int(input("Please enter another number from 1 till 64: "))
    Board[number-1]=CurrentUser

def chekHorizantal(Board):
    global Winner;
    firstindex=0
    lastindex=8
    summ=7
    for i in range(0,8):
        for j in range(firstindex,lastindex):
            if(j+3<=summ and Board[j]==Board[j+1] and Board[j]==Board[j+2] and Board[j]==Board[j+3] and Board[j]!="-"):
                Winner=CurrentUser
                return True
        firstindex=lastindex
        lastindex=lastindex+8
        summ=summ+7
def checkRow(Board):
    global Winner;
    firstindex=0
    lastindex=8
    for i in range(0,8):
        for j in range(firstindex,lastindex):
            if(j+24<64 and Board[j]==Board[j+8] and Board[j]==Board[j+16] and Board[j]==Board[j+24] and Board[j]!="-"):
                Winner=CurrentUser
                return True
        firstindex=lastindex
        lastindex=lastindex+8
def checkDiag(Board):
    global Winner
    firstindex=0
    lastindex=8
    m=8
    remember=8
    count=0
    for i in range(0,8):
        count=0
        for j in range(firstindex,lastindex):
            if(count<=4 and Board[j]==Board[j+9] and Board[j+9]==Board[j+18] and Board[j]==Board[j+27] and Board[j]!="-"):
                Winner=CurrentUser
                return True
            elif(count<=3 and Board[m]==Board[m+9] and Board[m+9]==Board[m+18] and Board[m]==Board[m+27] and Board[m]!="-"):
                Winner=CurrentUser
                return True
            elif(count>=4 and Board[j]==Board[j+7] and Board[j+7]==Board[j+14] and Board[j]==Board[j+21] and Board[j]!="-"):
                Winner=CurrentUser
                return True
            else:
                m=m+8
                count=count+1
        firstindex=firstindex+8
        lastindex=lastindex+8
        if(lastindex+27>64):
            break
        
        m=remember+1
        remember=m
        
def checkTie(Board):
    global GameRunning
    if("-" not in Board):
        GameRunning=True
        return True
def checkWin(Board):
    global GameRunning
    if(checkDiag(Board)==True or checkRow(Board)==True or chekHorizantal(Board)==True):
        GameRunning=True
        print("The Winner is ",CurrentUser)
    elif(checkTie(Board)==True):
        GameRunning=True
        print("It is a Tie")
def switchPlayer(Board):
    global CurrentUser
    if(CurrentUser=="X"):
        CurrentUser="O"
    else:
        CurrentUser="X"

def Computer(Board):
    rand=random.randint(1, 64)
    while(Board[rand-1]!="-"):
        rand=random.randint(1, 64)
    Board[rand-1]="O"
    
while(GameRunning==False):
    inputFromUser(Board)
    checkWin(Board)
    checkTie(Board)
    if(checkTie(Board)==True):
        break
    switchPlayer(Board)
    Computer(Board)
    PrintingBoard(Board)
    if(GameRunning==True):
        break
    switchPlayer(Board)
    checkWin(Board)
    checkTie(Board)
        