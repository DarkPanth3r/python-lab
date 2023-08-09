# 3.2.10 LAB The continue statement – the Ugly Vowel Eater

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter your word: \n")
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the for loop.
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)