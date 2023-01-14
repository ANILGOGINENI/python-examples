from optparse import Values
from secrets import choice
from tuple_intro import albums


while True:
    print()
    print("Please choose your album (invalid choice exits) : ")
    print()
    for index,(title,artist,year,song) in enumerate(albums):
        print("{}:{}\n".format(index+1,title))
        
        
    choice=int(input("Enter your choice here :"))
    if 1<=choice<=len(albums):
        song_list=albums[choice-1][3]
    else:
        break
   
    print("Please choose your song :")
    for index,(track_number,song) in enumerate(song_list):
        print("{}:{}".format(index+1,song))
        
    song_choice=int(input('Your choice : '))
    
    if 1<=song_choice<=len(song_list):
        title=song_list[song_choice-1][1]
        print("playing {}".format(title))
    
    print('*'*45)
        
        
         
    # for index,value in enumerate(albums):
    #     title,artist,year,song=value
    #     print(index+1,title,artist,year,song)
    # break
         