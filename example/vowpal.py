import os

train_sohrab = open("sohrab_train", "r", encoding='utf-8')
train_moshiri = open("moshiri_train", "r", encoding='utf-8')

moshiri_list = []
sohrab_list = []

for line in train_moshiri:
    if line != "\n":
        moshiri_list.append(line)

for line in train_sohrab:
    if line != "\n":
        sohrab_list.append(line)

train_sohrab.close()
train_moshiri.close()

test_sohrab = open("sohrab_test", "r", encoding='utf-8')
test_moshiri = open("moshiri_test", "r", encoding='utf-8')

moshiri_test = []
sohrab_test = []

for line in test_moshiri:
    if line != "\n":
        moshiri_test.append(line)

for line in test_sohrab:
    if line != "\n":
        sohrab_test.append(line)

print(moshiri_test)

test_moshiri.close()
test_sohrab.close()

vowpal_train = open("vowpal_train.txt", "a", encoding='utf-8')
vowpal_test = open("vowpal_test.txt", "a", encoding='utf-8')

if os.stat("vowpal_train.txt").st_size == 0:
    for i in range(len(moshiri_list) - 1):
        if i < len(sohrab_list):
            line = str("0 | " + moshiri_list[i])
            vowpal_train.write(line)
            line1 = str("1 | " + sohrab_list[i])
            vowpal_train.write(line1)
        else:
            break

vowpal_train.close()


if os.stat("vowpal_test.txt").st_size == 0:
    for i in range(len(moshiri_test) - 1):
        if i < len(sohrab_test):
            line = str("0 | " + moshiri_test[i])
            vowpal_test.write(line)
            line1 = str("1 | " + sohrab_test[i])
            vowpal_test.write(line1)
        else:
            break

vowpal_test.close()
