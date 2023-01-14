# names=["Anil","Ajay","Susanth","Rishi"]
# names.sort()
# print(names)
# # # for name in names:
# # #     print((name))
    
# # # print(names[2])
# # # names+=['AMMA']
# # # print(names)


# # # print('Mississipi'.count('M'))

# # a=b=c=d=e=f=names
# # print(a)
# # print(f)
# # print()
# # b.append('Nanna')

# # print(c)

# # print(a)

# available_parts=['computer','Mouse','Mouse mat','Key board','monitor','Hdmi cable']
# available_parts.sort()

# valid_choice=[]
# for i in range(1,len(available_parts)+1):
#     valid_choice.append(str(i))
# print(valid_choice)
# current_choice="_"

# computer_parts=[]

# while current_choice != '0':
    
    
#     if current_choice in valid_choice:
#         print('adding {}'.format(current_choice))
        
#         index=int(current_choice)-1
#         chosen_parts=available_parts[index]
#         computer_parts.append(chosen_parts)
#     #     if current_choice =='1':
#     #         computer_parts.append('computer')
#     #     elif current_choice =='2':
#     #         computer_parts.append('Mouse')
#     #     elif current_choice =='3':
#     #         computer_parts.append('Mouse mat')
#     #     elif current_choice =='4':
#     #         computer_parts.append('key board')
#     #     elif current_choice =='5':
#     #         computer_parts.append('Monitor')
#     #     elif current_choice=='6':
#     #         computer_parts.append('Hdmi cable')
            
#     else:
#         print('Please add options from the list :')
#         # print('1.computer')
#         # print('2.mouse')
#         # print('3.mouse mat')
#         # print('4.key boardr')
#         # print('5.Monitor')
#         # print('6.Hdmi cable')
#         # print('0. finish')
#         for part in available_parts:
#             print("{0} . {1}".format(available_parts.index (part)+1,part))
#     current_choice=input('enter a number : ')

# print(computer_parts)



num=[1,2,4,55,66,57,85,95,66,144,151,225,544,777,888,523,65,588,944,544]
#num = f.readlines()
for i in range(len(num)):
    name=str(num[i]).split(':')[0]
    name=num.split(':')[0]
    print(name)
# min_value=100
# max_value=200


# for index in range(len(num)-1,-1,-1):
#     if num[index]<min_value or num[index]>max_value:
#         print(index,num)
#         del num[index]
# print(num)







