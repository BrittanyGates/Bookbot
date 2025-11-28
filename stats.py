def count_words(book_text: str):
    total: int = 0
    text_list: list[str] = book_text.split()
    for word in text_list:
        total += 1
    return total


def count_characters(book_text: str):
    character_dict: dict = {}
    for letter in book_text:
        letter_lowered: str = letter.lower()

        if letter_lowered in character_dict:
            character_dict[letter_lowered] += 1
        else:
            character_dict[letter_lowered] = 1

    return character_dict


def key_sort(dictionary: dict):
    return dictionary["num"]


def sort_dict(dictionary: dict):
    list_to_sort: list = []
    for item in dictionary:
        new_dict: dict = {"char": item, "num": dictionary[item]}
        list_to_sort.append(new_dict)
    list_to_sort.sort(reverse=True, key=key_sort)

    return list_to_sort
