# 3.2.4 LAB Guess the secret number

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
guess = int(input("Enter your guess number: "))

while guess != secret_number:
    print("Ha ha! You're stuck in my loop!")
    guess = int(input("Try again: "))

print("""
Well done, muggle! 
You are free now.
""")