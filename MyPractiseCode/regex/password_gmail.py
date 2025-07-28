import re


def is_strong(password):
    # pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'
    return bool(re.match(pattern, password))


def clean_spaces(s):
    # return re.sub('/s+', '', s)
    li = ' '.join([item for item in s.split() if '' not in s.split()])
    return li


def extract_domain(url):
    # pattern = r"https?://(www\.)?([A-Za-z0-9.-]+)\.[a-z]{2,}"
    pattern = r"https://+[A-Za-z0-9]+\.[a-zA-Z0-9]+[A-Za-z]{2,}"
    match = re.search(pattern, url)
    return match.group() if match else None


def spilit_multiple():
    text = "apple,banana;grape orange"
    result = re.split(r'[;, ]+', text)
    print(result)  # ['apple', 'banana', 'grape', 'orange']


if __name__ == '__main__':
    print(is_strong("Pass@1234"))  # True
    print(clean_spaces("This   is   Python   "))  # "This is Python"
    print(extract_domain("https://www.google.com"))  # google
    print(extract_domain("http://openai.com"))  # openai
