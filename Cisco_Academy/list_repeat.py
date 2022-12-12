#Program removes repetead numbers on array
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
u_list = [] 

for number in my_list: 
    if number not in u_list: 
        u_list.append(number) 

print("The list with unique elements only:")
print(u_list)



