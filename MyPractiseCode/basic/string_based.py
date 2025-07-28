"""
Input: str = i.like.this.program.very.much
Output: hcum.yrev.margorp.siht.ekil.i
"""


def reverse_string():
    string = 'i.like.this.program.very.much'
    rev = string[::-1]
    print(rev)


"""
Input: str = i.like.this.program.very.much
Output: much.very.program.this.like.i
"""


def reverse_word_from_last():
    string = 'i.like.this.program.very.much'
    str_list_rev = string.split('.')[::-1]
    rev_string = '.'.join(str_list_rev)
    print(rev_string)


"""
input : Input: str = i.like.this.program.very.much
output : i.ekil.siht.margorp.yrev.hcum.
"""


def reverse_word_from_start():
    string = 'i.like.this.program.very.much'
    list_str = string.split('.')
    str_rev = ''
    for item in list_str:
        str_rev = str_rev + item[::-1] + '.'
    print(str_rev)


if __name__ == '__main__':
    # reverse_string()
    # reverse_word_from_last()
    reverse_word_from_start()
