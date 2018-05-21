# -*- coding: utf-8 -*-

from hazm import *
import os
from heapq import nlargest
import pickle

def normalizing(file, file_name):
    norm_file = open(file_name, "w+", encoding='utf-8')
    normalizer = Normalizer()
    for line in file:
        new_line = line.replace(".", "")
        new_line = new_line.replace("،", "")
        new_line = new_line.replace(":", "")
        new_line = new_line.replace("؟", "")
        new_line = new_line.replace("!", "")
        new_line = new_line.replace("«", "")
        new_line = new_line.replace("»", "")
        new_line = new_line.replace("؛", "")
        new_line = new_line.replace("–", "")
        if new_line == "\n":
            new_line = new_line.replace("\n", "")
        new_line = normalizer.normalize(new_line)
        norm_file.write(new_line)


def tokenizer(norm_file):
    data = {}
    #stemmer = Stemmer()
    for line in norm_file:
        word_list = word_tokenize(line)
        for item in word_list:
            #item = stemmer.stem(item)
            #print(item)
            if item not in data:
                data.update({item: 1})
            else:
                data[item] += 1
    return data


def prob_calculator(data, file_prob, wc, v):
    file = open(file_prob, "wb")
    for key in data.keys():
        data[key] = float(float(data[key] + 1)/(wc + v))
    pickle.dump(data, file)


def difference(data1, data2):
    dict = {}
    for key in data1.keys():
        if key in data2:
            #print(data1[key], data2[key])
            value = abs(data1[key] - data2[key])
            dict.update({key: value})
        if key not in data2:
            dict.update({key: data1[key]})
    for key in data2.keys():
        if key not in data1:
            dict.update({key: data2[key]})
    return dict

def categorize(list, data1, data2):
    categorized_dict = {}
    for item in list:
        if item in data1:
            categorized_dict.update({item: "sohrab"})
        if item in data2:
            categorized_dict.update({item: "moshiri"})
    return categorized_dict

def file_to_list(file):
    sentence_list = []
    for line in file:
        line = line.replace("\n", "")
        sentence_list.append(line)
    return sentence_list

# ************ Creating Normalized Files ************
file = open("sohrab_train", "r", encoding='utf-8')
normalizing(file, "sohrab_norm.txt")
file.close()
# ************ Tokenizing File ************
file = open("sohrab_norm.txt", "r", encoding='utf-8')
data_sohrab = tokenizer(file)
sohrab_data = open("sohrab_data.pkl", "wb")
pickle.dump(data_sohrab, sohrab_data)
sohrab_data.close()

# ************ Creating Normalized Files ************
file = open("moshiri_train", "r", encoding='utf-8')
normalizing(file, "moshiri_norm.txt")
file.close()
# ************ Tokenizing File ************
file = open("moshiri_norm.txt", "r", encoding='utf-8')
data_moshiri = tokenizer(file)
moshiri_data = open("moshiri_data.pkl", "wb")
pickle.dump(data_moshiri, moshiri_data)
moshiri_data.close()

# ************ Loading Tokenized File ************
sohrab_data = pickle.load(open("sohrab_data.pkl", "rb"))
moshiri_data = pickle.load(open("moshiri_data.pkl", "rb"))

vocab = []
for key in sohrab_data.keys():
    vocab.append(key)
for key in moshiri_data.keys():
    if key not in vocab:
        vocab.append(key)
vocab_size = len(vocab)
print(vocab_size)

most_effective_words = nlargest(int(vocab_size/10), difference(sohrab_data, moshiri_data),
                                key=difference(sohrab_data, moshiri_data).get)
print(most_effective_words)
print(len(most_effective_words))

categorized_words = categorize(most_effective_words, sohrab_data, moshiri_data)

mallet_file = open("mallet_file.txt", "a", encoding="utf-8")
file_sohrab = open("sohrab_norm.txt", "r", encoding='utf-8')
file_moshiri = open("moshiri_norm.txt", "r", encoding="utf-8")

if os.stat("mallet_file.txt").st_size == 0:
    counter = 0
    sohrab_sents = file_to_list(file_sohrab)
    moshiri_sents = file_to_list(file_moshiri)
    print(len(sohrab_sents))
    for i in range(len(moshiri_sents)):
        dict_counter = 0
        mallet_file.write("{} {}".format(counter, "sohrab"))
        for key in categorized_words.keys():
            if i < len(sohrab_sents):
                if categorized_words[key] == "sohrab" and key in sohrab_sents[i]:
                    mallet_file.write(' ' + key)
            if dict_counter == len(categorized_words.keys()) - 1:
                mallet_file.write('\n')
            dict_counter += 1
        mallet_file.write("{} {}".format(counter, "moshiri"))
        dict_counter = 0
        for key in categorized_words.keys():
            if categorized_words[key] == "moshiri" and key in moshiri_sents[i]:
                mallet_file.write(' ' + key)
            if dict_counter == len(categorized_words.keys()) - 1:
                mallet_file.write('\n')
            dict_counter += 1
        counter += 1
mallet_file.close()

prob_calculator(sohrab_data, "prob_s.pkl", 8733, vocab_size)
prob_calculator(moshiri_data, "prob_m.pkl", 9510, vocab_size)


prob_s = pickle.load(open("prob_s.pkl", "rb"))
prob_m = pickle.load(open("prob_m.pkl", "rb"))

# difference1 = difference(data_s, data_m)

p_moshiri = 0.56
p_sohrab = 0.46
