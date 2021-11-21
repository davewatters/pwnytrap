##
# PwnyTrap
#
# Created by David Watters 2021
# https://github.com/davewatters
#
# PwnyTrap queries the HaveIBeenPwned.com API to determine if a given password
# or email address has been compromised in a data breach.
#
# The HIBP database and API were created by Troy Hunt
# https://troyhunt.com ; https://haveibeenpwned.com
#
# Python3
##
import textwrap
import json
import hashlib
import requests


CREDS_FILE = 'creds.json'
HIBP_PWD_API_URL = 'https://api.pwnedpasswords.com/range/'
HIBP_API_URL = 'https://haveibeenpwned.com/api/v3/'
URL_HEADERS = {'User-Agent': 'PwnyTrap'}


def cls():
    '''
    Clears the screen and places cursor at top left
    Similar to *nix terminal clear or Win cls
    '''
    print("\033[H\033[J", end="")
    print('123456789+' * 8) # 123456789+123456789+
    return


def disp_main_page():
    '''
    Displays the main greeting and menu options
    '''
    cls()
    s = """
        PwnyTrap - Catch bad pa$$words using the Have I Been Pwned API\n\n
        Options:\n
        1. Show Help screen\n
        2. Check password\n
        3. Check email address\n
        4. Lookup breach info\n
    """
    print(textwrap.dedent(s))
    return


def help_screen():
    '''
    Displays the help information screen
    '''
    cls()
    s = """
        PwnyTrap Help\n

        Lots of helpful info goes here.\n
        TODO explain checking passowrd pwnage
        TODO explain checking email address pwnage\n
        TODO Explain the HIBP API\n
        TODO Include a link to the HIBP site and also it's FAQ page\n

        Finally, in case you were wondering...\n
        PwnyTrap is pronounced 'Pony Trap'.  It comes from the leetspeak word 'pwn'
        meaning to be beaten or compromised in some way.\n
        For an explanation check this link: https://en.wikipedia.org/wiki/PWN\n
    """
    print(textwrap.dedent(s))
    input("Enter to return to the main screen..")
    return


def check_password():
    '''
    Accepts user input for password to check
    Checks password for inclusion in HIBP breached passwords database
    '''
    print('\nChecking password..')
    passwd = input('Enter password to check: ')
    paswd_hash = hashlib.sha1(passwd.encode('utf-8')).hexdigest()
    print(f'SHA-1 hash digest of password: {paswd_hash}')
    search_hash = paswd_hash[:5].upper()
    resp = requests.get(HIBP_PWD_API_URL + search_hash)
    matches = resp.text.splitlines()
    count = 0
    for s in matches:
        h, c = s.split(':')
        if search_hash + h == paswd_hash.upper():
            count = int(c)
            break
    
    if count > 0:
        print("Bad news - you've been pwned!")
        print(f"Password appeared {count:,} times in the database.")
        print("This password should never be used again.")
    else:
        print("Good news! Password not found in database.")
        print("Remember, this does NOT mean that it is a GOOD password, just that it hasn't yet appeared in an online dump.")

    input("\nEnter to return to the main menu..")
    return


def main():
    '''
    Main program loop
    '''
    while True:
        disp_main_page()
        opt = input("Enter your choice [1-4, or q to quit]: ")
        if opt == 'q':
            print('Goodbye.')
            break
        elif opt == '1':
            help_screen()
        elif opt == '2':
            check_password()


##
main()
##
