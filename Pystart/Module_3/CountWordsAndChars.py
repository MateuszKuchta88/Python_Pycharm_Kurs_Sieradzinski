sentence = input('Give me the sentence to analyze on number of words and characters: ')

nof_chars = len(sentence.replace(' ', ''))
nof_words = len(sentence.split())

print(f'In this sentence we have {nof_words} words and {nof_chars} characters.')