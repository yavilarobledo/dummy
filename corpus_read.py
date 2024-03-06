
def count_word_occurrences(file_path, token):
    with open(file_path, 'r') as file:
        corpus_text = file.read()
        count = corpus_text.lower().count(token.lower())
    return count
