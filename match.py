import re
str='Python is easy language'
pattern='Python'
result=re.match(pattern, str)
print(result.group())
print(result.start())
print(result.end())