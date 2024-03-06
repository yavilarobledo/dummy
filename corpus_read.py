file_path='/content/corpus.txt'
token='School'
def read_corpus(file_path):
    with open(file_path, 'r') as file:
        corpus_text = file.read()
    return corpus_text

def count_word_occurrences(corpus, token):
    words = corpus.split()
    return words.count(token)
