def word_count():
    with open('test_data.txt', 'r+') as file:
        content = file.read()
        words = content.split()
        vowel = 'aeiou'
        word_containing_vowel = [item for item in words if set(item).intersection(vowel)]
        print(word_containing_vowel, len(word_containing_vowel))


if __name__ == '__main__':
    word_count()
