import re
test_str = "govinda is my name"
new_str = re.sub(r'[aeiou]','',test_str)
print(new_str)


