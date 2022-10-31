# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:53:34 2022

@author: mh22adu
"""
import pandas as pd
import clean_up as cl

with open("big_data.txt", 'r') as text:
    all_words = []
    counter = 0
    for line in text:
        words = line.split()
        counter = counter+1
        for word in words:
            word = cl.clean(word)
            all_words.append(word)
print (counter)
print ('number of words = ',len(all_words))


df_words = pd.DataFrame(data= all_words, columns = ("words",))
df_counts = df_words["words"].value_counts()
print (df_counts)