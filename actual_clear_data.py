"""
    Creates - once more - clear data suitable for the extraction of the sentences we need.
"""

import csv
import os
import glob
import pandas as pd

punctuation = {'.', '?', '!'}
verbs = set()

def spot_tag(file, tag):    # spots a specific annotation level 
                            # (the annotation is slightly different in some files) 
    df = pd.read_excel(file)
    header = list(df.columns.values)
    if tag in header:
        return header.index(tag)

def list_to_string(ls):
    string = ""
    for item in ls:
        string += str(item)
        string += " "
    return string

with open('prefixed_verbs_right_wrong.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            verbs.add(row[0])

verbs.remove('Verb')

### the following code was run once and only used in order to clear out the data.

dafr = list()
small = list()

path = "MorphSem_L2-Corpus" 
for infile in glob.glob(os.path.join(path, "*.xlsx")):
    df = pd.read_excel(infile)
    all_values = df.values.tolist()
    tagziel = spot_tag(infile, "ZH2:ZH2") # storing the maximal target hypothesis
    tagerror = spot_tag(infile, "ZHverb:verbfehlertyp_all")
    for row in all_values:
        if tagziel != None:
            if tagerror != None:
                small.extend((row[0], row[2], row[tagziel], row[tagerror]))
                dafr.append(small)
                small = list()

myFile = open('cleardata-part2_v1.csv', 'w')
with myFile:
    writer = csv.writer(myFile, delimiter='\t')
    writer.writerows(dafr)
myFile.close()

# The following lines contain the code for the separation of the sentences.

tokens = list() # originally all 
small_token = list()

lemmas = list() # comparison with following
small_lemma = list()

ziele = list() # contains possible target lemma, in case of an error
small_zh = list()

error = list() # in order to see if the tag 'sem' is included
small_error = list()

f = open('cleardata-part2_v1.csv', 'rt')
for line in f:
    line = line.split()
    if line[0] not in punctuation:
        small_token.append(line[0])
        small_lemma.append(line[1])
        small_zh.append(line[2])
        small_error.append(line[3])
    else: # punctuation included, new nested list / sentence stored in the four big lists
        small_token.append(line[0])
        small_lemma.append(line[1])
        small_zh.append(line[2])
        small_error.append(line[3])

        tokens.append(small_token)
        lemmas.append(small_lemma)
        ziele.append(small_zh)
        error.append(small_error)

        small_token = list()
        small_lemma = list() 
        small_zh = list() 
        small_error = list()

f.close()

# Extraction of the sentences containing an error.
# If a nested list in the big list 'error' contains a 'sem' tag, then the whole sentence
# (tokens) is included in observed_sentences.
# Its respective ZH sentence is stored in target_sentences.

observed_sentences = list()
target_sentences = list()

for i in range(len(tokens)):
    for j in range(len(tokens[i])):
        if lemmas[i][j] in verbs:
            if 'sem' in error[i][j]:
                originalsentence = list_to_string(tokens[i])
                if ' nan ' in originalsentence:
                    originalsentence = originalsentence.replace(' nan ', ' ')
                observed_sentences.append(originalsentence)
                correctsentence = list_to_string(ziele[i])
                if ' nan ' in correctsentence:
                    correctsentence.replace(' nan ', ' ')
                target_sentences.append(correctsentence)

# writing the files with the correct and the wrong sentences, respectively

MyFile = open('correct_sentences.txt','w')
for element in target_sentences:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()

MyFile = open('wrong_sentences.txt','w')
for element in observed_sentences:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()

