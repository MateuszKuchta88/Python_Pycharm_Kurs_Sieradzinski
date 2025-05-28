sentence = 'raz raz dwa dwa trzy dwa dwa raz trzy'
words_list = sentence.split()
count_dict = {}
update_dict = {}

for word in words_list:
    if word not in count_dict:
        update_dict = {word:1}
        count_dict.update(update_dict)
    else:
        count_dict[word] += 1

print(count_dict)