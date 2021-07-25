# Write your code here
import random

random.seed()
li_of_words = ["python", "java", "kotlin", "javascript"]
print('''H A N G M A N''')
while True:
    user_choice = input('Type "play" to play the game, "exit" to quit:')
    if user_choice == "exit":
        break
    elif user_choice != "play":
        continue
    else:
        pass
    cnt, user_letters = 8, ""
    chosen_word = random.choice(li_of_words)
    firstString = chosen_word
    secondString = "-" * len(firstString)
    while cnt != 0:
        translation = chosen_word.maketrans(firstString, secondString)
        translated_string = chosen_word.translate(translation)
        print()
        print(translated_string)  # print(translated_string, chosen_word)
        user_letter = input(f"Input a letter: ")
        if len(user_letter) != 1:
            print("You should input a single letter")
            continue
        if user_letter not in "qwertyuiopasdfghjklzxcvbnm":
            print("Please enter a lowercase English letter")
            continue
        if user_letter not in user_letters:
            user_letters += user_letter
        else:
            print("You've already guessed this letter")
            continue
        if user_letter in chosen_word:
            firstString = firstString.replace(user_letter, ".")  # print(firstString)
            if firstString.count(".") == len(firstString):
                print()
                print(chosen_word)
                print("""You guessed the word!
You survived!""")
                break
        else:
            print("That letter doesn't appear in the word")
            cnt -= 1
    else:
        print("You lost!")
    print()
