#Khoa Duong
#Assignment 6
#Create a program that collect user's phone#, ssc#, and zip codes;display it if it's valid
#1. Import re module (re.match) to work with regular expressions and make sure informations entered are matched.
#2, Create a main function to collect datas using regular expressions.
#2. Display result if it is valid.

import re

#Get informations from the users.
def main():
    phone_number = input('Enter your phone number (ex: 012- or (012)-456-7890):')
    social_security = input('Enter your Social Security number (ex: 123-45-6789):')
    zip_code = input('Enter your zipcode number (ex: 12345 or 12345-6789):')

    #Print the validated results.
    print('\nValidation Results:')
    
    if valid_number(phone_number, "phone"):
        print(f'Your phone number: {phone_number}')
    else:
        print('please enter your phone number follow the right example format')
    if valid_number(social_security, "ssn"):
        print(f'Your Social Security number: {social_security}')
    else:
        print('please enter your SSN follow the right example format')
    if valid_number(zip_code, "zip"):
        print(f'Your Zipcode :{zip_code}')
    else:
        print('please enter your Zipcode follow the right example format')

#Make sure the informations matches the format.
def valid_number(number, number_type):
        #using regex to validate number.
        patterns = {
            "phone" : r'^\(?\d{3}\)?[-]?\d{3}[-]?\d{4}$',
            "ssn" : r'^\d{3}-\d{2}-\d{4}$',
            "zip" : r'^\d{5}(-\d{4})?$'
        }
        return bool(re.match(patterns.get(number_type, ""), number))



if __name__ == '__main__':
    main()
