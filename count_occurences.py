"""
    A function that takes a lemma and a verb list as input.
    Counts the occurence of each verb in the lemma list.
"""

def occurence_count(file_corpus, file_verbs):
    
    prefixed_verb_occurence = dict()

    f = open(file_verbs, 'rt')
    for line in f:
        line = line.replace('\n', '')
        prefixed_verb_occurence[line] = 0
    f.close()

    f = open(file_corpus, 'rt')
    for line in f:
        for verb in prefixed_verb_occurence:
            if verb in line:
                prefixed_verb_occurence[verb] += 1
    f.close()

    return prefixed_verb_occurence

significant_three = dict() 

occ = occurence_count('corpus_sentences_lemma.txt','prefixed_verbs.txt')
for k, v in occ.items():
    if v >= 3:
        significant_three[k] = ''

