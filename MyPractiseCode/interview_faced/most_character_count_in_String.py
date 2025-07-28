# Find the maximum repeated character in a string without having o(n2) complexity.
def max_character_count():
    str_test = "govinda kumar gupta"
    uniq_ch = []
    for i in str_test:
        if i not in uniq_ch:
            uniq_ch.append(i)
    print(uniq_ch)

    ch_count_ch = {}

    for i in uniq_ch:
        ch_count_ch[i] = str_test.count(i)
    print(ch_count_ch)

    dic = dict(sorted(ch_count_ch.items(), key=lambda d: d[1]))
    max_char = max(ch_count_ch, key=ch_count_ch.get)
    print(max_char)
    print(f"Character with the maximum count: '{max_char}' with count {ch_count_ch[max_char]}")


max_character_count()
