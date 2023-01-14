#High Low guessing game
low=1
high=1000
print("guess in the range between {} and {}".format(low,high))
input(" press Enter to start ")

guesses=1
while True:
    print("\t guess in the range between {} and {}".format(low,high))
    guess=low+(high-low)//2
    high_low=input("my guess is {}. should i guess high or low? "
                   "enter h or l or c, if my guess was correct "
                   .format(guess).casefold())
    if high_low == "h":
        low=guess+1
    elif high_low  == "l":
        high=guess-1
    elif high_low=="c":
        print("i got in {} guesses".format(guesses))
        break
    else:
        print(" please enter h or l or c")
    guesses+=1
        
    
    