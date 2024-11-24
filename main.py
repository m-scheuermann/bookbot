def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    print(f"This book has {number_of_words} words.")
    number_of_characters = count_characters(text)
    print("This book has a lot of characters! Here's a list of them and how many there are:\n", number_of_characters, sep="")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    words_number = len(words)
    return words_number

def count_characters(text):
    lowered_text = text.lower()
    characters = {}
    for character in lowered_text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

main()