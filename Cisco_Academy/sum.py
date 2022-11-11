# Sum of natural numbers up to num

#num = int(input("Enter a number: ")) 

#if num < 0:
#   print("Please enter a positive number")
#else:
#   sum = 0
   
   # use while loop to iterate until zero
#   while(num > 0):
#       sum += num
#       num -= 1
#       print("sum: ", sum)
#       #print("num: ", num)
#   
#print("The result is", sum)


number = int(input('Enter a positive number: '))

my_sum = 0
i=0

while i <= number:
    my_sum = my_sum + i
    print(my_sum)
    i+=1

print("The sum of the numbers is", my_sum)