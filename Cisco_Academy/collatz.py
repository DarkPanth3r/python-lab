# https://en.wikipedia.org/wiki/Collatz_conjecture

number = int(input('Enter a positive number: '))

i = 0
while number != 1 and number > 0:
    i += 1 
    if (number % 2) == 0: #if number is even
        number = number / 2
    else:
        number = 3 * number + 1
    print(int(number))

print("Steps = ", i)