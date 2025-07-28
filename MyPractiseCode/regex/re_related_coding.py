import re


def verify_email():
    gmail = "govindakg543@gmai.com"
    pattern = r'[A-Za-z0-9]+@+[A-Za-z0-9]+\.[a-zA-Z0-9]{2,}'
    match_ob = re.search(pattern, gmail)
    if match_ob is not None:
        print("matched")
    else:
        print("not matched")


def search_word():
    # matches words that start with an uppercase letter followed by one or more word characters
    string = "hello Words"
    match_word = re.search(r'[A-Z]+[a-z]{2,}', string)
    print(match_word)


def verify_dob():
    date = '2054-12-15'
    match_date = re.search(r'\d{4}-\d{2}-\d{2}', date)
    print("date-matched", match_date)


def using_compile():
    date = 'I am Govinda. my dob is 2054-12-15'
    comp = re.compile(r'\d{4}-\d{2}-\d{2}')
    mat_wor = comp.search(date)
    print("by compile", mat_wor)


def sub_string():
    string1 = "Welcome to, india rahul."
    new_str = re.sub(r'[  ,.]', ';', string1, )
    print(new_str)


def split_string():
    str1 = "My  .--NameIs...///----   . Adhitesh---123-.....   ..."
    list_of_str = re.split(r'[.  ]', str1)
    print(list_of_str)


if __name__ == '__main__':
    # verify_email()
    # search_word()
    # verify_dob()
    # using_compile()
    # sub_string()
    split_string()
