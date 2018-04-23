from random import shuffle
from hazm import *

# ************ Generating Test and Train Data for Sohrab ************

file = open("sohrab_norm.txt", encoding='utf-8')
result = file.read().split("\n")[:-1]
shuffle(result)

test = result[:int(len(result)/10)]
train = result[int(len(result)/10):]

train_file = open("sohrab_train", "w", encoding='utf-8')
for item in train:
    train_file.write(item)
    train_file.write("\n")
train_file.close()

test_file = open("sohrab_test", "w", encoding='utf-8')
for item in test:
    test_file.write(item)
    test_file.write("\n")
test_file.close()

# ************ Generating Test and Train Data for Moshiri ************

file = open("moshiri_norm.txt", encoding='utf-8')
result = file.read().split("\n")[:-1]
shuffle(result)

test = result[:int(len(result)/10)]
train = result[int(len(result)/10):]

train_file = open("moshiri_train", "w", encoding='utf-8')
for item in train:
    train_file.write(item)
    train_file.write("\n")
train_file.close()

test_file = open("moshiri_test", "w", encoding='utf-8')
for item in test:
    test_file.write(item)
    test_file.write("\n")
