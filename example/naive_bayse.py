# -*- coding: utf-8 -*-

from hazm import *
import pickle

file_moshiri = open("moshiri.txt", "r", encoding='utf-8')
file_sohrab = open("sohrab.txt", "r", encoding='utf-8')


def normalizing(file, file_name):
    norm_file = open(file_name, "w+", encoding='utf-8')
    normalizer = Normalizer()
    for line in file:
        new_line = line.replace(".", "")
        new_line = new_line.replace("،", "")
        new_line = new_line.replace(":", "")
        new_line = new_line.replace("؟", "")
        new_line = new_line.replace("!", "")
        new_line = new_line.replace(">>", "")
        new_line = new_line.replace("<<", "")
        new_line = new_line.replace("؛", "")
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
            value = data1[key] - data2[key]
            dict.update({key: value})
    return dict


# ************ Creating Normalized Files ************
normalizing(file_sohrab, "sohrab_norm.txt")
# ************ Tokenizing File ************
file = open("sohrab_train", "r", encoding='utf-8')
data_sohrab = tokenizer(file)
sohrab_data = open("sohrab_data.pkl", "wb")
pickle.dump(data_sohrab, sohrab_data)
sohrab_data.close()

# ************ Creating Normalized Files ************
normalizing(file_moshiri, "moshiri_norm.txt")
# ************ Tokenizing File ************
file = open("moshiri_train", "r", encoding='utf-8')
data_moshiri = tokenizer(file)
moshiri_data = open("moshiri_data.pkl", "wb")
pickle.dump(data_moshiri, moshiri_data)
moshiri_data.close()

# ************ Loading Tokenized File ************
data_s = pickle.load(open("sohrab_data.pkl", "rb"))
data_m = pickle.load(open("moshiri_data.pkl", "rb"))

sohrab_data = pickle.load(open("sohrab_data.pkl", "rb"))
moshiri_data = pickle.load(open("moshiri_data.pkl", "rb"))

vocab = []
for key in sohrab_data.keys():
    vocab.append(key)
for key in moshiri_data.keys():
    if key not in vocab:
        vocab.append(key)
vocab_size = len(vocab)

prob_calculator(data_s, "prob_s.pkl", 8733, vocab_size)
prob_calculator(data_m, "prob_m.pkl", 9510, vocab_size)

prob_s = pickle.load(open("prob_s.pkl", "rb"))
prob_m = pickle.load(open("prob_m.pkl", "rb"))

# difference1 = difference(data_s, data_m)

p_moshiri = 0.56
p_sohrab = 0.46
