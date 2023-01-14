from nltk.tokenize import RegexpTokenizer
import pandas as pd
import numpy as np


class ProfHinglishFilter:
    def __init__(self, gaali):

        self.input_text = gaali
        self.gaaliSent = gaali
        # self.gaaliSent = re.sub(r'[^a-zA-Z0-9 ]',r'',self.input_text)
        self.gaaliSent = self.gaaliSent.lower()
        print(self.gaaliSent)

    def extra_letters(self, s):
        original = s[0]
        edited = s[0]
        for i in s[1:]:
            if i != original:
                edited += i
                original = i
        return edited

    def filter_gaali(self):
        # tokenizer = RegexpTokenizer(r'\w+')

        # word_tokinize = tokenizer.tokenize(self.gaaliSent)
        word_tokinize = self.gaaliSent.split()
        edits = []
        for i in word_tokinize:
            edits.append(self.extra_letters(i))

        data_set = pd.read_csv('profanity_final.csv')
        new = data_set.to_numpy()
        new = new.flatten()
        data_set1 = []
        for i in new:
            data_set1.append(self.extra_letters(i))

        new = data_set1
        print(new, "data")
        output = []

        for i in range(0, len(edits)):
            found = True
            for j in range(0, len(new)):
                if edits[i] == new[j]:
                    found = False
                    temp = edits[i].replace(edits[i], "***")
                    if temp=='***':
                        pass
                    output.append(temp)
                    break
            if (found):
                output.append(word_tokinize[i])

        print(output)

        final_text = " ".join(output)

        print(final_text)
        return [str(final_text), str(self.gaaliSent)]
