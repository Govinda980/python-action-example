with open('testdata.txt', 'r') as file:
    content = file.read()
    print(content)
    word = content.split(" ")
    vowel = ['a', 'e', 'i', 'o', 'u']
    word_list = [item for item in word if set(item).intersection(set(vowel))]
    print(word_list, len(word_list))
