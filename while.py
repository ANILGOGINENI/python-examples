# # i=0
# # while i<10:
# #     print(" i is now {}".format(i))
# #     i+=1
# available_exits=["north","south","east","west"]
# chosen_exit=""
# while chosen_exit not in available_exits:
#     chosen_exit=input("please choose a direction :")
#     if chosen_exit.casefold() == "quit":
#         print("Game Over")
#         break

# print("you chose right direction!")
# for i in range(0, 100, 7):
#     print(i)
#     if i>0 and i%16==0:
#         break
#with continue
for i in range(0,20):
    if i%3==0 or i%5==0:
        continue
    print(i)
print('.............................................................................')
#with out continue
for x in range(21):
    if x%3!=0 and x%5!=0:
        print(x)