import random


brd = [[10,2,3],[4,5,6],[7,8,9]]
player1 = 'NULL'
player2 = 'NULL'

def main():

    stillPlaying = True
    while stillPlaying:
        mainMenu()
        clrBoard()
        game()


def mainMenu():
    userChoice = input('Would you like to play tic-tac-toe? (y/n)\n')
    if userChoice == 'n':
        exit()

    global player1, player2
    player1 = input("Please enter Player 1's name\n")
    player2 = input("Please enter Player 2's name\n")

def clrBoard():
    global brd
    brd = [[10,2,3],[4,5,6],[7,8,9]]

def game():
    #randomly assigns first turn
    turn = random.randint(1,1000) % 2

    #loop while no one has won
    stillPlaying = True
    while stillPlaying == True:
        #print the board
        printBrd()

        #who's turn is it? take their turn
        playTurn(turn)
        
        #if win() returns true, someone won, go away
        print(win())
        if int(win()) == 1:
            print ("You Win!")
            stillPlaying = False
        #toggle between each player's turn
        turn = (turn + 1) % 2

def printBrd():
    global brd

    for o in range(3):
        for d in range(3):
            if brd[o][d] == 0:
                print('X', end='')
            elif brd[o][d] == 1:
                print('O', end='')
            elif brd[o][d] == 10:
                print(1, end='')
            else:
                print(brd[o][d], end='')

            print(' ', end='')

        print('\n')


def playTurn(player):
    global brd

    print("%s, Take your turn" % (player1 if player == 0 else player2))
    
    userChoice = input('Please input which number you would like place your %s\n' % ('X' if player == 0 else 'O'))

    counter = 1
    for o in range(3):
        for d in range(3):
            if counter == int(userChoice):
                brd[o][d] = int(player)
            counter += 1

def win():
    count = 0
    playerX = 0
    playerO = 0

    for o in range(3):
        for d in range(3):
            if brd[o][d] == 0:
                playerX += 1
            elif brd[o][d] == 1:
                playerO += 1
        
        if playerX == 3 or playerO == 3:
            return 1
        playerX = 0
        playerO = 0

    for o in range(3):
        for d in range(3):
            if brd[d][o] == 0:
                playerX += 1
            elif brd[d][o] == 1:
                playerO += 1
        
        if playerX == 3 or playerO == 3:
            return 1
        playerX = 0
        playerO = 0

    if brd[0][0] == 0 and brd[1][1] == 0 and brd[2][2] == 0 or brd[0][2] == 1 and brd[1][1] == 1 and brd[2][0] == 1:
        return 1
    return 0



if __name__ == '__main__':
    main()