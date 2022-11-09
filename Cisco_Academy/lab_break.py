#3.2.1.9 LAB: The break statement - Stuck in a loop

sword = "chupacabra"

while True:
    word = input("Enter secret word: \n")
    if word == sword:
        print("You've successfully left the loop.")
        break
    if word != sword:
        print("You are wrong! Try again: ")