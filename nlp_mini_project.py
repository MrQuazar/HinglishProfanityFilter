
import nltk

from nltk.tokenize import RegexpTokenizer
import re
import pandas as pd
import numpy as np

class ProfHinglishFilter:

  def __init__(self, gaali):

    self.input_text = gaali
    self.gaaliSent = re.sub(r'[^a-zA-Z0-9 ]',r'',self.input_text)
    self.gaaliSent = self.gaaliSent.lower()
    print(self.gaaliSent)

  def filter_gaali(self):
    tokenizer = RegexpTokenizer(r'\w+')

    word_tokinize = tokenizer.tokenize(self.gaaliSent)

    print(word_tokinize)

    data_set = pd.read_csv('profanity_filter.csv')

    data_set.head()

    new = data_set.to_numpy()
    new = new.flatten()
    new

    output = []

    for i in range(0, len(word_tokinize)):
      found = True
      for j in range(0, len(new)):
        if word_tokinize[i]==new[j]:
          found = False
          temp = word_tokinize[i].replace(word_tokinize[i], "***")
          output.append(temp)
          break
      if(found):
          output.append(word_tokinize[i])

    print(output)

    final_text = " ".join(output)

    print(final_text.title())
    return [str(final_text.title()),str(self.gaaliSent)]
