dictionary = {'dog':'pies', 'cat':'kot', 'cow':'krowa',
              'mouse':'mysz', 'bird':'ptak'}

translate_way = input('Tell me what you want to do.\nIf you would like to translate words from polish to english type "en",\nif you would like to translate words from english to polish type "pl": ')

if translate_way.lower() == 'en':
    word = input("Give me word in english you'd like to translate to polish: ")
    if word in dictionary:
        print(f'Word {word} in polish means "{dictionary[word]}".')
    else:
        print('There is no such word in our dictionary.')
elif translate_way.lower() == 'pl':
    word = input("Give me word in polish you'd like to translate to english: ")
    if word in dictionary.values():
        print(f'Word {word} in english means "{list(dictionary.keys())[list(dictionary.values()).index(word)]}".')
    else:
        print('There is no such word in our dictionary.')
else:
    print('Error')

