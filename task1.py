# -*- coding: utf-8 -*-

import pandas as pd, time


def anagrams(input_string):
    if len(input_string) <= 1:
        return input_string
    else:
        temp = []
        for anagram in anagrams(input_string[1:]):
            for i in range(len(input_string)):
                tmp_string = anagram[:i] + input_string[0:1] + anagram[i:]
                temp.append(tmp_string)
        return temp


def get_data():
    data = pd.read_excel("PersianWords.xlsx")
    data = data['*Total farsi Word (Moin+openoffice.fa+wikipedia)']
    mySet = set([])
    for i in data:
        mySet.add(i)
    return mySet


given_word = input("string: ")
anagrams = anagrams(given_word)
print(anagrams)
data = get_data()

list1 = []
for anagram in anagrams:
    if anagram in data:
        list1.append(anagram)

print(list1)
