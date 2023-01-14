menu=[['egg','bacon'],['egg','cheese','spam'],['beef','cheese','bacon','spam'],['spam','spam','spam']]


for meal in menu:
    for item in meal:
        if item !="spam":
            print(item)
        print()
    
    # for index in range(len(meal)-1,-1,-1):
    #     if meal[index]=='spam':
    #         del meal[index]
    #     print(meal)
            # if 'spam' not in menu:
    #     print(menu)
    #     for  item in menu:
    #         print(item)
    # else:
    #     print("{0} has spam score of {1}".format(menu,menu.count('spam')))