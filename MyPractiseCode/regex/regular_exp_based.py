import re

"""
re.findall – this module is used to search for “all” occurrences that match a given pattern.
re.sub – it is used to substitute the matched RE pattern with given text
re.match – The match function is used to match the RE pattern to string with some optional flags
re.search – search method takes a regular expression pattern and a string and searches for that pattern with the string.

"""

# pattern = r'\w{3}' #atches exactly three alphanumeric characters
# pattern = r'\b[A-Z]\w+\b' #matches words that start with an uppercase letter followed by one or more word characters
# pattern = r'\b[A-Z]\w*'
# The re.compile() function in Python is used to create a compiled regular expression object for reuse, which can improve performance.

# r'\b[a - zA - Z0 - 9._ % +-]+ @ [a - zA - Z0 - 9. -] +.[a - zA - Z]{2, }\b'
# re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
str1 = "govindakg543@gmail.com"
pattern = r'\b[a-zA-Z0-9._%-]+@[a-zA-A0-9.-]+\.[A-Za-z]{2,}\b'
se = re.match(pattern, str1)
print(se)

pattern = r'\d{2}-\d{2}-\d{4}'
text = "Date of birth: 12-31-1990"
result = re.findall(pattern, text)
print(result)

pattern = r'[A-Za-z0-9_]+'
text = "Hello World_123"
result = re.findall(pattern, text)
print(result)
# \b specifying word boundary.
pattern = r'\b\d{3}\b'
text = "123 4567 890 12 3456"
result = re.findall(pattern, text)
print(result)

string1 = "Welcome to, india rahul."
new_str = re.sub(r'[ ,.]', ';', string1)
print(new_str)

str1 = "My  .--NameIs...///----   . Adhitesh---123-.....   ..."
str_list = re.split(r'[ .]', str1)
print(str_list)

