# import re

# text_to_search = "abcdefghijkl\nmnopqrstuvwxyz"
# pattern = re.compile(r".")
# res = re.finditer(pattern, text_to_search)
# for row in res:
#     print(row)

# # Types of Strings - STRING, formatted string, raw string - (r"") - escape sequences are ignored

import re
fp = open("RegEx.txt","r")
data = fp.read()

pattern = re.compile(r"")