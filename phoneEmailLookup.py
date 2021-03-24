#! python 3

import re, pyperclip

# Create regex for phone numbers
phoneRegex = re.compile(r'''

(
((\d{3})|(\(\d{3}\)))?  # optional area code
(\s|-)?                   # first separator
\d{3}                  # first 3 digits
-                      # second separator
\d{4}                  # last 4 digits
((ext(\.)?\s|x)        # extension word (optional)
 (\d{2,5}))?           # extension number (optional)
)

''', re.VERBOSE)

# Create regex for email addresses
emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+  # name
@
[a-zA-Z0-9_.+]+  #domain

''', re.VERBOSE)

# Get text off clipboard
text = pyperclip.paste()

# Extract email/phone
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

cleanedNumbers = []
for phoneNumber in extractedPhone:
    cleanedNumbers.append(phoneNumber[0])

# Copy extract to clipboard
results = '\n'.join(cleanedNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)