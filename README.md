# Simple and Prefix Verbs in Second Language Learning

The following document lists all modules & files used for the project.

The corpus data is in MorphSem_L2-Corpus.

### 1. QUANTITATIVE ANALYSIS

- `preprocessing.py` initial preprocessing and extraction of the layers needed
	Input: Corpus
	Output: cleardata.csv, corpus_sentences_lemma.txt

- `cleardata.csv` file originally used for the extraction of all prefix verbs
- `corpus_sentences_lemma.txt` lemmatized sentences in the corpus (used in order to count occurences later)

- `prefix_rough.py` module for the spotting of all prefix verbs in the corpus
	Input: cleardata.csv
	Output: verbs.csv

- `verbs.csv` noisy data, initial list of all prefix verbs
- `regex_for_verbs.py` regular expression for the sorting out of the verbs relevant to the project

- `prefixed_verbs.txt` manually processed prefix verb list

- `count_occurences.py` module used for the extraction of the most frequent verbs

- `only_the_most_significant.csv` list containing simple and prefix verbs (manually modified)

- `preprocessing_simple.py` module for the extraction of simple verbs occurences
	Input: Corpus, only_the_most_significant.csv
	Output: simple_verbs_right_wrong.csv

- `preprocessing_prefix.py` module for the extraction of prefix verbs occurences
	Input: prefixed_verbs_right_wrong.csv (manually created, not included), cleardata.csv
	Output: prefix_verbs_right_wrong.csv

The following two lists have been modified manually:

- `simple_verbs_right_wrong.csv` list with the simple verbs in question, including correct / wrong occurences
- `prefix_verbs_right_wrong.csv` list with the prefix verbs in question, including correct / wrong occurences


### 2. QUALITATIVE ANALYSIS

For this part, sentences containing prefix verbs in a wrong context (& their correct counterparts) are needed.

- `actual_clear_data.py` module for the extraction of sentences
	Input: Corpus
	Intermediate output / input: cleardata-part2_v1.csv
	Final output: wrong_sentences.txt, correct_sentences.txt

- `cleardata-part2_v1.csv` contains only the annotation layers needed for this task: tokens, lemmata, extended target hypothesis, error type 

- `wrong_sentences.txt` contains sentences with a prefix verb used in a wrong context
- `correct_sentences.txt` contains sentences from the target hypothesis
