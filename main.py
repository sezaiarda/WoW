from itertools import chain, combinations
from collections import Counter


def find_words_with_subclasses(words, given_letters):
    results = set()
    max_length = len(given_letters)

    letters_subclasses = list(chain.from_iterable(combinations(given_letters, r) for r in range(1, len(given_letters) + 1)))

    for word in words:
        if len(word) > max_length or len(word) <= 2:
            continue

        for letters_subclass in letters_subclasses:
            counter = Counter(letters_subclass)
            get = True
            for letter in list(word):
                if letter not in letters_subclass:
                    get = False
                    break
            if get:
                if Counter(list(word)) != counter:
                    continue
                results.add(word)
    return results


def main():
    with open("words.txt", "r", encoding="utf-8") as f:
        words = f.readlines()
    words = [word.strip() for word in words]

    while True:
        given_letters = input("\n\nEnter the given letters: ").lower()

        results = find_words_with_subclasses(words, given_letters)

        for result in set(results):
            print(result)


if __name__ == "__main__":
    main()

