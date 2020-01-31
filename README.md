# simple_prefix_verbs_german

cleardata.csv > file originally used for the extraction of all prefix verbs

verbs.csv > noisy data, initial list of all prefix verbs
regex_for_verbs.py > regular expression for the sorting out of the verbs relevant to the project


PART 2 - QUALITATIVE ANALYSIS

For this part, sentences containing prefix verbs in a wrong context (& their correct counterparts) are needed.

actual_clear_data.py > module for the extraction of sentences
	Input: Corpus
	Intermediate output / input: cleardata-part2_v1.csv
	Final output: wrong_sentences.txt, correct_sentences.txt

cleardata-part2_v1.csv > contains only the annotation layers needed for this task: tokens, lemmata, extended target hypothesis, error type 

wrong_sentences.txt > contains sentences with a prefix verb used in a wrong context
correct_sentences.txt > contains sentences from the target hypothesis