import pandas as pd
import numpy as np
import csv
import os


def extra_letters(s):
    original = s[0]
    edited = s[0]
    for i in s[1:]:
        if i != original:
            edited += i
            original = i
    return edited


data_set = pd.read_csv('profanity_filter.csv')
new = data_set.to_numpy()
new = new.flatten()
data_set1 = []
for i in new:
    data_set1.append(extra_letters(i))


def lister(l):
    return [[word] for word in l]


rows = lister(data_set1)
print(rows)
fields = ['Foul Words']

filename = "profanity_edited.csv"

# writing to csv file
with open(filename, 'w', encoding='utf-8', errors='ignore') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

result = ""
with open("./profanity_edited.csv", "r+", encoding='utf-8',
          errors='ignore') as file:
    for line in file:
        if not line.isspace():
            result += line

with open("./profanity_final.csv", "w", encoding='utf-8',
          errors='ignore') as finalfile:
    finalfile.write(result)

import os

if (os.path.exists(filename) and os.path.isfile(filename)):
    os.remove(filename)
    print("file deleted")
else:
    print("file not found")
