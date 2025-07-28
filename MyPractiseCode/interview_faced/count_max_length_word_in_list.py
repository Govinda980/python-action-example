def find_largest_word(words):
    words.sort(key=len)
    print(words[-1])


def find_largest_word_without_builtin(words):
    max_item = 0
    index = 0
    for idx, value in enumerate(words):
        if len(value) > max_item:
            max_item = len(value)
            index = idx
    print(words[index])

         


if __name__ == '__main__':
    words = ["apple", "banana", "cherry", "dragonfruit", "kiwi"]
    find_largest_word(words)
    find_largest_word_without_builtin(words)
