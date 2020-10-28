import re
str='Python is easy language'
pattern='easy'
result=re.search(pattern, str)
print(result.group())
print(result.start())
print(result.end())