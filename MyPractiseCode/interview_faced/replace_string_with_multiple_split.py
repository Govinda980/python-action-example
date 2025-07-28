# Replace maximum 2 occurrences of space, comma, or dot with a colon, in regex.
# import re
# String1= "Welcome to, india rahul."
# str1 = re.sub('[ ,.]',';', String1, count=2)
# print(str1)
import re


def count_length_of_valid_last_string():
    str1 = "My  .--NameIs...///----   . Adhitesh---123-.....   ..."
    # str_list = str1.split('.')
    split_text = re.split(r'[. ]+', str1)
    last_valid_str = len([item for item in split_text if item != ''][-1])
    print(last_valid_str)


def replace_max_two_occ_space_comma_dot():
    str1 = "Welcome to, india rahul."
    new_str = re.sub(r'[ ,.]', ':', str1, count=2)
    print(new_str)


count_length_of_valid_last_string()
replace_max_two_occ_space_comma_dot()
