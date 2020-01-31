import csv

tokens = list()
lemmas = list()
ziele = list() # contains possible target lemma, in case of an error
cat = list() # if applicable: contains the category of the complex verb.

# set for reference

tags = {'tok', 'pos', 'lemma', 'ctok:ctok', 'ctok:ctokpos', 'ctok:ctoklemma', 
        'learner:macro', 'ZH0:ZH0', 'ZH0:ZH0Diff', 'ZH0:ZH0S', 'ZH0:ZH0pos', 'ZH0:ZH0posDiff', 
        'ZH0:ZH0pos.1', 'ZH0:ZH0gposDiff', 'ZH0:ZH0lemma', 'ZH0:ZH0lemmaDiff', 'ZH1:ZH1', 
        'ZH1:ZH1Diff', 'ZH1:ZH1pos', 'ZH1:ZH1S', 'ZH1:ZH1posDiff', 'ZH1:ZH1gpos', 'ZH1:ZH1gposDiff', 
        'ZH1:ZH1lemma', 'ZH1:ZH1lemmaDiff', 'ZH2:ZH2', 'ZH2:ZH2Diff', 'ZH2:ZH2pos', 'ZH2:ZH2S', 
        'ZH2:ZH2posDiff', 'ZH2:ZH2lemma', 'ZH2:ZH2lemmaDiff', 'ZHverb:ZHverb', 'ZHverb:ZHverbDiff', 
        'ZHverb:ZHverbpos', 'ZHverb:ZHverbposDiff', 'ZHverb:ZHverblemma', 'ZHverb:ZHverblemmaDiff', 
        'ZHverb:verbkategorie', 'ZHverb:verblemma', 'ZHverb:verbfehlertyp_all', 'ZHverb:verbform', 
        'learner:TXTstructure', 'ZH1:ZH1DepID', 'ZH1:dep(ZH1>ZH1)', 'ZH1:func(dep(ZH1--ZH1))', 'ZH1depTOK', 
        'ZH1TopoFields1', 'ZH1TopoFields2', 'ZH1TopoFields3', 'ZH1Const1', 'ZH1Const2', 'ZH1Const3', 
        'ZH1Const4', 'ZH1Const5', 'ZH1Const6', 'ZH1Const7', 'ZH1Const8'}

# in the following lines, all complex verbs found in erroneous sentences
# are extracted and listed alphabetically.

f = open('cleardata.csv', 'rt')
for line in f:
    line = line.split()
    tokens.append(line[0])
    lemmas.append(line[1])
    ziele.append(line[2])
    cat.append(line[3])
f.close()

categories = {'vpart', 'vpräf', 'ppart', 'ppräf', 'vpartx', 'ppartx', 'vpräfx'}
allverbs = set() # will contain all complex verbs appearing to be in erroneous sentences

f = open('cleardata.csv', 'rt')
for line in f:
    line = line.split()
    if line[3] in categories:
        allverbs.add(line[1])
f.close()

allverbs = list(allverbs)
allverbs.sort()

myFile = open('verbs.csv', 'w')
for item in allverbs:
    myFile.write(item + '\n')
myFile.close()

# in both allverbs and the file verbs.csv, there are errors
# further processing is needed
