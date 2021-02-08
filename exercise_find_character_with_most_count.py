# find out the most used character in this sentence:

# My Solution:
# sentence = "This is a common interview question"
# sentence = sentence.lower()
# sentence = [*sentence]

# count = 0
# test = {item: count+1 for item in sentence}
# print('Test:', test)

# for character in sentence:
#     count = 0
#     for x in sentence:
#         if character == x:
#             count = count+1
#             print(character, count)
#             {**test, character: count}

# print('Test:', test)

# Mosh Solution:
from pprint import pprint
sentence = "This is a common interview question"

# step 1 Dictionary: convert into a dictionary! its poserfull because the key is unique
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
pprint(char_frequency, width=1)

# step 2 Sorting: Remember Dictionaries are unordered collection and cannot be sorted so you need to convert a dictionary to a tupple:
char_requency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

# step 3 display:
print('Most use char is: ', char_requency_sorted[0])
