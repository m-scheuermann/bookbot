def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"This document has {number_of_words} words.")
    print()
    number_of_characters = count_characters(text)
    characters_as_list = dict_to_list(number_of_characters)
    characters_as_list.sort(reverse=True, key=sort_on)
    for character in characters_as_list:
        print(f"The '{character["character"]}' character was found {character["amount"]} times")
    print("--- End report ---")


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
        elif character.isalpha() == True:
            characters[character] = 1
    return characters


def dict_to_list(dict):
    dict_as_list = [{"character": key, "amount" : value} for key, value in dict.items()]
    return dict_as_list


def sort_on(dict):
    return dict["amount"]


main()