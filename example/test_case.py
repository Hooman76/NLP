import pickle
from functools import reduce
from hazm import *
import math

data_s = pickle.load(open("prob_s.pkl", "rb"))
data_m = pickle.load(open("prob_m.pkl", "rb"))

test_sohrab = open("sohrab_test", "r", encoding='utf-8')
test_moshiri = open("moshiri_test", "r", encoding='utf-8')

count_correct_s = 0
count_all_s = 0

count_correct_m = 0
count_all_m = 0

p_moshiri = 0.56
p_sohrab = 0.46

sohrab_data = pickle.load(open("sohrab_data.pkl", "rb"))
moshiri_data = pickle.load(open("moshiri_data.pkl", "rb"))

vocab = []
for key in sohrab_data.keys():
    vocab.append(key)
for key in moshiri_data.keys():
    if key not in vocab:
        vocab.append(key)
vocab_size = len(vocab)

for line in test_sohrab:
    line = line.strip("\n")
    count_all_s += 1
    sentence = word_tokenize(line)
    prob_per_word_s = []
    prob_per_word_m = []
    for item in sentence:
        if item in data_s:
            prob_per_word_s.append(data_s[item])
        else:
            prob_per_word_s.append(1/(vocab_size + 8733))
        if item in data_m:
            prob_per_word_m.append(data_m[item])
        else:
            prob_per_word_m.append(1/(vocab_size + 9510))
    if len(prob_per_word_s) >= 2:
        prob_s = reduce(lambda x, y: x*y, prob_per_word_s) * p_sohrab
        #print(prob_s)
    elif len(prob_per_word_s) == 1:
        prob_s = prob_per_word_s[0] * p_sohrab
    if len(prob_per_word_m) >= 2:
        prob_m = reduce(lambda x, y: x * y, prob_per_word_m) * p_moshiri
    elif len(prob_per_word_m) == 1:
        prob_m = prob_per_word_m[0] * p_moshiri
    if prob_s > prob_m:
        count_correct_s += 1
        #print("sohrab was guessed correctly")

prob_s = 0
prob_m = 0

for line in test_moshiri:
    line = line.strip("\n")
    count_all_m += 1
    sentence = word_tokenize(line)
    prob_per_word_s = []
    prob_per_word_m = []
    for item in sentence:
        if item in data_s:
            prob_per_word_s.append(data_s[item])
        else:
            prob_per_word_s.append(1/(vocab_size + 8733))
        if item in data_m:
            prob_per_word_m.append(data_m[item])
        else:
            prob_per_word_m.append(1/(vocab_size + 9510))
    if len(prob_per_word_s) >= 2:
        prob_s = reduce(lambda x, y: x*y, prob_per_word_s) * p_sohrab
    elif len(prob_per_word_s) == 1:
        prob_s = prob_per_word_s[0] * p_sohrab
    if len(prob_per_word_m) >= 2:
        prob_m = reduce(lambda x, y: x * y, prob_per_word_m) * p_moshiri
    elif len(prob_per_word_m) == 1:
        prob_m = prob_per_word_m[0] * p_moshiri
    if prob_m > prob_s:
        count_correct_m += 1
        #print("moshiri was guessed correctly")

sohrab_recall = float(count_correct_s/count_all_s)
moshiri_recall = float(count_correct_m/count_all_m)
print("recall:\n sohrab: {}\n moshiri: {}".format(sohrab_recall, moshiri_recall))

sohrab_precision = float(count_correct_s/(count_correct_s + (count_all_m - count_correct_m)))
moshiri_precision = float(count_correct_m/(count_correct_m + (count_all_s - count_correct_s)))
print("precision:\n sohrab: {}\n moshiri: {}\n".format(sohrab_precision, moshiri_precision))
