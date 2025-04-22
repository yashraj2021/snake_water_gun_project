'''
1 for snake
-1 for water
0 for gun'
'''
import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1 : "Snake",-1 : "Water", 0 : "Gun"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its DRAW")

else:
    '''

    if (computer == -1 and you == 1):  # (computer - you) = -2
        print("YOU WIN")

    elif(computer == -1 and you == 0): # (computer - you) = -1
        print("YOU LOSE")

    elif(computer == 1 and you == -1): # (computer - you) = 2
        print("YOU LOSE")

    elif(computer == 1 and you == 0): # (computer - you) = 1
        print("YOU WIN")

    elif(computer == 0 and you == -1): # (computer - you) = 1
        print("YOU WIN")
        
    elif(computer == 0 and you == 1): # (computer - you) = -1
        print("YOU LOSE")

    else:
        print("Something went wrong!")

        THE BELOW LOGIC IS WRITTEN ON THE BASIS OF VALUE OF (computer - you)


    '''

    if((computer - 1) == -1 or (computer - you) == 2):
        print("You Lose")
    else:
        print("You Win")



