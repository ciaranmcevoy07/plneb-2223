import re
str='O tst, que ta muito tst'
str2 = 'tst'
a = re.search(str2 + r'(.+?)', str, re.IGNORECASE)
new_str = str.lower()
str = re.sub(r'\b' + str2 + r'\b', 'pneu', new_str)
print(str)