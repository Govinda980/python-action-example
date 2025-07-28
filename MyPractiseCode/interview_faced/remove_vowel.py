import re


def remove_vowel():
    test_str = "govinda is my name"
    new_str = re.sub(r'[aeiouAEIOU]', '', test_str)
    print(new_str)


def remove_consonant():
    test_str = "Govinda is my name"
    vowel = 'aeiouAEIOU '
    new_str = ''.join([ch for ch in test_str if ch in vowel])
    print(new_str)


remove_consonant()
remove_vowel()