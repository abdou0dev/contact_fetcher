import re, pyperclip
pyperclip.set_clipboard('wl-clipboard')
# Phone number pattern
phone_pattern = re.compile(r'''
(\+\d{1,3}-|\+\d{1,3}\s|00\d{1,3}\s)? # country code
(\(\d{3}\)\s|\d{3}-|\d{3}\.)? # Area code with separator
(\d{3}) # First three digits
(-|\.|\s)? # Separator
(\d{4}) # Four last digits
''', re.VERBOSE)
# email address pattern
email_pattern = re.compile(r'\b[^\s@"]+@[^\s@\.]+\.[^\s@]+\b')

def main():
    
    # Matching phone numbers.
    number_match = phone_pattern.findall(pyperclip.paste())
    # Extracting phone numbers into one format.
    cleaned = []
    if number_match:
        for i in range(len(number_match)):
            number_match[i] = list(number_match[i])
            for j in range(len(number_match[i])):
                number_match[i][j] = number_match[i][j].strip('()-. ')
            number_match[i] = ''.join(number_match[i])
            if number_match[i].startswith('00'):
                cleaned.append( '+' + number_match[i][2:])
            else:
                cleaned.append(number_match[i])
        # Printing Numbers.
        print('Phone numbers: ')
        for number in cleaned:
            print(' ' + number)
    else:
        print('There might be no phone numbers in your text, make sure you copied the right text.')

    # Matching Emails.
    email_match = email_pattern.findall(pyperclip.paste())
    if email_match:
        # Printing Emails
        print('Email addresses: ')
        for email in email_match:
            print(' ' + email) 
    else:
        print('There might be no emails in your text, make sure you copied the right text.')
    
    pyperclip.copy('\n\n'.join(cleaned + email_match))
    print('Done')
    
    
main()

