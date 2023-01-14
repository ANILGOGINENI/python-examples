import random
answer = random.randint(1,10)
print(answer)
guess=0 
print("please guess a numberbetween 1 to 10 : ")
while guess !=answer:
    guess=int(input())
    if guess==answer:
        print("you got it first time")
    else:
        if guess<answer:
            print("guess higher")
        else:
            print(" guess lower")
    # guess=int(input())
    # if guess==answer:
    #     print("well done it is correct ")
    # else:
    #     print("better luck next time ")