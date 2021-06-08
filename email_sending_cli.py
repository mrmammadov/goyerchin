import argparse
import smtplib
import os
import re
import sys

# Environment Variables
email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

# # CLI Installation
# my_parser = argparse.ArgumentParser(prog='email', description='List of all the files in the path')

# my_parser.add_argument('Person', metavar='person', type=str, help='the path to list')
# my_parser.add_argument('Email', metavar='email', type=str, help='the path to list')


# args = my_parser.parse_args()

# person = args.Person
# email_to = args.Email

# msg = f'''
# To: {email_to}

# Dear {person},

# I am going to be graduating from FAU with a degree in Information Systems (Masters) and looking for roles related to Python. 
# I have included my CV in the attachments.
# Looking forward to hear from you!

# Best Regards,
# Gulu Mammadli
# '''



def send_email(email_from, email_to, mail):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email, password)

        pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        match = re.match(pattern, email_from)

        if match:
            for e in email_to:
                smtp.sendmail(email_from, e, mail)
        else:
            return 'Incorrect email format!'

    print('Email sent!')