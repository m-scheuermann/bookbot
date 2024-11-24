def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    print(number_of_words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text_string):
    words = text_string.split()
    words_number = len(words)
    return words_number

main()