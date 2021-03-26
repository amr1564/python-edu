#! python3

import re, pyperclip

#Create dollar amount regex
dollarRegex = re.compile(r'''

(
(?:\d,)*
\d{1,3}
\.
\d{2}
)

''', re.VERBOSE)

text = pyperclip.paste()

extractedAmounts = dollarRegex.findall(text)
for i,j in enumerate(extractedAmounts):
    if "," in j:
        extractedAmounts[i] = j.replace(",", "")

sum = sum(list(map(lambda x: float(x), extractedAmounts)))

print (f"The total dollar amount is {sum}")