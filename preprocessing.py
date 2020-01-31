
import csv
import os
import glob
import pandas as pd

def spot_tag(file, tag): # spots a specific annotation level - actually pretty useful 
    df = pd.read_excel(file)
    header = list(df.columns.values)
    if tag in header:
        return header.index(tag)

def make_sentences(dataframe, number): # creates sentences out of a dataframe (list of lists basically)
    punctuation = {'.', '?', '!'}
    text = str()
    sentences = list()
    for token in dataframe:
        word = token[number]
        if isinstance(word, str):
            if word in punctuation:
                text += word
                sentences.append(text)
                text = str()
            else:
                text += word
                text += " "
    return sentences 

new_df = [] # dataframe that will contain the corpus, but with the annotation levels needed: token, lemma, category, target lemma, 
small = list()

path = "MorphSem_L2-Corpus" 
for infile in glob.glob(os.path.join(path, "*.xlsx")):
    df = pd.read_excel(infile)
    all_values = df.values.tolist()
    tagcat = spot_tag(infile, "ZHverb:verbkategorie")
    tagform = spot_tag(infile, 'ZHverb:verbform')
    tagfehler = spot_tag(infile, 'ZHverb:verbfehlertyp_all')
    for row in all_values:
        if tagcat != None:
            if tagform != None:
                if tagfehler != None:
                    small.extend((row[0], row[2], row[tagcat], row[tagform], row[tagfehler]))
                    new_df.append(small)
                    small = list()

lemma_sentences = make_sentences(new_df, 1)

f = open('corpus_sentences_lemma.txt', 'w')
for sentence in lemma_sentences:
    f.write(sentence)
    f.write('\n')
f.close()

myFile = open('cleardata.csv', 'w')
with myFile:
    writer = csv.writer(myFile, delimiter='\t')
    writer.writerows(new_df)
myFile.close()

