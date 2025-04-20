import random
'''
snake = -1
water = 1 
gun = 0 
'''

computer = random.choice([-1, 0, 1]) # imported a random module to choose a random number between [-1,1,0]
youstr = input("Enter what you want to throw:")
dict = {'s':-1, 'w':1, 'g':0} # you select what to throw form these three keys
reversedict = {-1:"snake", 1:'water', 0:"gun"} # made another dictionary to print what you and computer chose 

you = dict[youstr]

print(f"Computer chose {reversedict[computer]}\nYou chose {reversedict[you]}") # prints what you chose

if computer == you:
    print('It was a draw')

# 
# else:
#     if computer == -1 and you == 1: -2
#         print("You Lose!")
#     elif computer == -1 and you == 0: -1
#         print("You Win!")
#     elif computer == 1 and you == -1: 2
#         print("You Win!")
#     elif computer == 1 and you == 0: 1
#         print("You Lose!")
#     elif computer == 0 and you == -1: 1
#         print("You Lose!")
#     elif computer == 0 and you == 1: -1 
#         print("You Win!")
#     else:
#         print("There was an error")
else:
    if (computer - you == -2) or (computer - you == 1):
        print("you Lose!")
    else:
        print("You Win")

# Logic of this code is: if we subtract computer - you and it is -2 or 1 then you are losing 
# otherwise you are winning. 
# but it's better to write the code fully for visual clarity. or comment out the thing 