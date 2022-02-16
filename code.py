from random import random
import numpy as np
import random


# taking out the five-letter words from the word list
"""with open("./words.txt") as f:
    five_word = []
    for line in f:
        if len(line) == 6:
            five_word.append(line[:-1])"""

# saving the five-letter words as a different file
"""with open("./five-words.txt","w") as f:
    for w in five_word:
        f.write(w + "\n")"""

with open("./five-words.txt") as f:
    words = set()
    for line in f:
        words.add(line[:-1])

possible_words = words
print("Input data as (1)letter followed by its correct position or (2)only letter if it is not in the word or (3)letter followed by its incorrect position followed by '.' , for example : 'd2 f g5.' ")
while True:
    data = input().split()
    if len(data) == 0:
        break
    rm = set()
    for rule in data:
        if len(rule) == 1:
            for w in possible_words:
                if rule in w:
                    rm.add(w)
            for w in rm:
                if w in possible_words:
                    possible_words.remove(w)
        elif len(rule) == 2:
            right = set()
            for w in possible_words:
                if w[int(rule[1])-1] == rule[0]:
                    right.add(w)
            possible_words = right
        elif len(rule) == 3:
            right = set()
            for w in possible_words:
                #print(rule[0],int(rule[1])-1,type(int(rule[1])-1))
                if rule[0] in w and w[int(rule[1])-1] != rule[0]:
                    right.add(w)
            possible_words = right
        else:
            print(rule, "format is wrong")
        
    print("possible words are : ", " ".join(possible_words))

    