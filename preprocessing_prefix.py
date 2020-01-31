import csv

prefix_verbs = dict()

with open('prefixed_verbs_right_wrong.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            prefix_verbs[row[0]] = {'correct':0, 'wrong':0}

del(prefix_verbs['Verb'])

with open('cleardata.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        if row[1] in prefix_verbs:
            if 'sem' in row[4]:
                prefix_verbs[row[1]]['wrong'] += 1
            else:
                prefix_verbs[row[1]]['correct'] += 1

df_simple = [['Verb', 'Correct instances', 'Wrong instances']]
small = []

for verb in prefix_verbs:
    small.append(verb)
    small.append(prefix_verbs[verb]['correct'])
    small.append(prefix_verbs[verb]['wrong'])
    df_simple.append(small)
    small = list()

myFile = open('prefix_verbs_right_wrong.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(df_simple)
