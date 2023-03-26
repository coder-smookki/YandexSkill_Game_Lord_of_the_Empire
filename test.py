import re


a = '[shuffle]'


b = re.findall(r"\d+", a)

print(b)