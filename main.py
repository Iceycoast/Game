import random
'''
snake = -1
water = 1 
gun = 0 
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter what you want to throw:")
dict = {'s':-1, 'w':1, 'g':0}
reversedict = {-1:"snake", 1:'water', 0:"gun"}

you = dict[youstr]

print(f"Computer chose {reversedict[computer]}\nYou chose {reversedict[you]}")

if computer == you:
    print('It was a draw')
else:
    if computer == -1 and you == 1:
        print("You Lose!")
    elif computer == -1 and you == 0:
        print("You Win!")
    elif computer == 1 and you == -1:
        print("You Win!")
    elif computer == 1 and you == 0:
        print("You Lose!")
    elif computer == 0 and you == -1:
        print("You Lose!")
    elif computer == 0 and you == 1:
        print("You Win!")
    else:
        print("There was an error")
    