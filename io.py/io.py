# text=open('E:\\\Python\\io.py\\test.txt','r')
# for line in text:
#    
#     #print(len(line))
# text.close()

with open('E:\\\Python\\io.py\\test.txt','r') as text:
    test=text.read()
    for character in reversed(test):
        print(character,end='')
    # for line in text:
    #     print(line.lstrip())