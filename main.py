import random

'''
1 for snake
-1 for water
0 for gun

'''




# Your choice
youstr = input("Enter your choice: ")
youDict = {
    "snake": 1 ,
    "water" : -1,
    "gun" : 0  }
you = youDict[youstr]
print(f"Your choice: {youstr}")

# computer's choice
list = ["snake", "water", "gun"]
random_element = random.choice(list)


computer = youDict[random_element]
print(f"Computer's choice: {random_element}")



if(computer==you):
    print("Its a draw")
else:
    if(computer==-1 and you == 1):
        print("You win!")
    elif(computer==-1 and you == 0):
        print("You lose!")
    elif(computer==1 and you == -1):
        print("You lose!")
    elif(computer==1 and you == 0):
        print("You win!")
    elif(computer==0 and you == 1):
        print("You lose!")
    elif(computer==0 and you == -1):
        print("You win!")
    else:
        print("Something went wrong!!")


















