item={
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five"
}


pantry_items=['chicken','eggs','butter','spam','lemon']
# new_dict=dict.fromkeys(pantry_items,0)
# print(new_dict)
# keys=items.keys()
# print(keys)

# for item in items.keys():
#     print(item)


#Update method in dict methods

# d2={
    
#     7:"lucky seven",
#     6:"super six",
#     10:"high ten"
    
# }

# item.update(d2)
# for key,value in item.items():
#     print(key,value)
    
# print()

# item.update(enumerate (pantry_items))
# for key,value in item.items():
#     print(key,value)



#PRINT VALUES OF DICT METHOD

a=item.values()
b=len(item)

item[10]="big ten"
print(a)
print(b)

print("four" in item)
print("eight" in item)
print(9 not in item)



for key,value in item.items():
    if value=="five":
        print(f"{item[key]} was found with key {key}")

