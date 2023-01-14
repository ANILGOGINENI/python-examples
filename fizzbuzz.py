def fizz_buzz(number: int,)->str:
    if number%15==0:
        return "fizz buzz"
    elif number%3==0:
        return "fizz"
    elif number %5==0:
        return "buzz"
    else:
        return str(number)
# for i in range(1,101):
#     print(fizz_buzz(i))
input("play fizzbuzz")
print()

next_num=0
while next_num<99:
    next_num+=1
    print(fizz_buzz(next_num))
    next_num+=1
    correct_answer=fizz_buzz(next_num)
    #p_a=input("your go : ")
    p_a=correct_answer
    if p_a!=correct_answer:
        print("you lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("well done you reached {}".format(next_num))