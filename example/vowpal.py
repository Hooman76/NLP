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

test_moshiri.close()
test_sohrab.close()

vowpal_train = open("vowpal_train.txt", "a", encoding='utf-8')
vowpal_test = open("vowpal_test.txt", "a", encoding='utf-8')

if os.stat("vowpal_train.txt").st_size == 0:
    for i in range(len(moshiri_list) - 1):
        if i < len(sohrab_list):
            line = str("-1 | " + moshiri_list[i])
            vowpal_train.write(line)
            line1 = str("1 | " + sohrab_list[i])
            vowpal_train.write(line1)
        else:
            break

vowpal_train.close()


if os.stat("vowpal_test.txt").st_size == 0:
    for i in range(len(moshiri_test) - 1):
        if i < len(sohrab_test):
            line = str("-1 | " + moshiri_test[i])
            vowpal_test.write(line)
            line1 = str("1 | " + sohrab_test[i])
            vowpal_test.write(line1)
        else:
            break

vowpal_test.close()


res = open("prediction.txt", "r")
counter = 0
moshiri_pred = []
sohrab_pred = []
for line in res:
    if counter%2 == 0:
        if float(line)<0:
            moshiri_pred.append(-1)
        else:
            moshiri_pred.append(1)
    else:
        if float(line)>0:
            sohrab_pred.append(1)
        else:
            sohrab_pred.append(-1)
    counter+=1

true_moshiri = 0
true_sohrab = 0

for item in moshiri_pred:
    if item == -1:
        true_moshiri += 1

for item in sohrab_pred:
    if item == 1:
        true_sohrab += 1

accuracy_moshiri = true_moshiri/(len(sohrab_pred)+len(moshiri_pred))
accuracy_sohrab = true_sohrab/(len(sohrab_pred)+len(moshiri_pred))

precision_moshiri = true_moshiri/len(moshiri_pred)
precision_sohrab = true_sohrab/len(sohrab_pred)

recall_moshiri = true_moshiri/(len(sohrab_pred) - true_sohrab + true_moshiri)
recall_sohrab = true_sohrab/(len(moshiri_pred) - true_moshiri + true_sohrab)

print("sohrab results: ")
print("sohrab accuracy:" + str(accuracy_sohrab))
print("sohrab precision:" + str(precision_sohrab))
print("sohrab recall:" + str(recall_sohrab) + "\n")

print("moshiri results: ")
print("moshiri accuracy:" + str(accuracy_moshiri))
print("moshiri precision:" + str(precision_moshiri))
print("moshiri recall:" + str(recall_moshiri))
