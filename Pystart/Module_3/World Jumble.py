from random import shuffle, choice

words = ["python", "apple", "jungle", "rockstar", "iceman", "waterfall"]

picked_word = choice(words)
picked_word_as_list = list(picked_word)
shuffle(picked_word_as_list)
picked_word_shuffled = ''.join(picked_word_as_list)

for i in range (3):
    print(picked_word_shuffled)
    user_answer = input("Give me this word: ")
    if user_answer == picked_word:
        print("Great! You're right.")
        quit()
    else:
        print("Yyy... No? Please try again.")

print("Unfortunately, you lost.")