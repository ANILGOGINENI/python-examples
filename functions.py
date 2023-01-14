# from tkinter import Y
# from unittest import result


# def multiply(x,y):
#     result= x * y 
#     return result
# ans=multiply(6,8)
# print(ans)


def is_palindrome(string):
    return string[::-1]==string

word=input("Enter a word to check : ")

if is_palindrome(word.casefold()):
    print("{} is palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))

