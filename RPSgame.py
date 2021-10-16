import random
def gameWin(computer, you):
    if computer == you:
        return None
    elif computer == 'Rock':
        if you=='Scissors':
            return False
        elif you=='Paper':
            return True
    elif computer == 'Paper':
        if you=='Rock':
            return False
        elif you=='Scissors':
            return True
    elif computer == 'Scissors':
        if you=='Paper':
            return False
        elif you=='Rock':
            return True

def Result(you):
    print(f"Computer chose {computer}")
    print(f"You chose {you}")
    a = gameWin(computer, you)
    if a == None:
        print("The game is a tie!!!!!!!!!!!!!!")
    elif a:
        print("You Win!!!!!!!")
    else:
        print("You Lose!!!!!!")


print("Comp Turn: Rock, Paper or Scissor!!!")
randNo = random.randint(1, 3) 
if randNo == 1:
    computer = 'Rock'
elif randNo == 2:
    computer = 'Paper'
elif randNo == 3:
    computer= 'Scissors'

you = input('''Your Turn: 
Rock, Paper or Scissor?\n''')
Result(you)