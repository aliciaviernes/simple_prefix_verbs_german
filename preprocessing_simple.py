"""
    For all the verbs from the list that occur thrice or more, correct and wrong instances are counted and then
    normalised, in order to give the right / wrong percentage for each verb.
"""

import csv
import os
import glob
import pandas as pd

def spot_tag(file, tag): # spots a specific annotation level
    df = pd.read_excel(file)
    header = list(df.columns.values)
    if tag in header:
        return header.index(tag)

lemma_zielhypothese = list() # dataframe that will contain the corpus, but with the annotation levels needed: lemma, target lemma 
small = list()

path = "MorphSem_L2-Corpus"
for infile in glob.glob(os.path.join(path, "*.xlsx")):
    df = pd.read_excel(infile)
    all_values = df.values.tolist()
    tagziel = spot_tag(infile, "ZH0:ZH0lemma")
    for row in all_values:
        if tagziel != None:
            small.extend((row[2], row[tagziel]))
            lemma_zielhypothese.append(small)
            small = list()

simple_errors = dict()

# data filtered - most frequent and relevant verbs used.

with open('only_the_most_significant.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|') # rows are lists
    for row in spamreader:
        simple_errors[row[0]] = {'right': 0, 'error': 0}

# counting correct and wrong occurences

for pair in lemma_zielhypothese:
    if pair[0] in simple_errors:
        if pair[0] == pair[1]:
            simple_errors[pair[0]]['right'] += 1
        else:
            simple_errors[pair[0]]['error'] += 1

df_simple = [['Verb', 'Correct instances', 'Wrong instances']]
small = []

for verb in simple_errors:
    small.append(verb)
    small.append(simple_errors[verb]['right'])
    small.append(simple_errors[verb]['error'])
    df_simple.append(small)
    small = list()

# creating initial file

myFile = open('simple_verbs_right_wrong.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(df_simple)
