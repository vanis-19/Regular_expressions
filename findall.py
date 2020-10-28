import re
str='Python is easy language  is to learn'
pattern='is'
result=re.findall(pattern, str)
print(result)
