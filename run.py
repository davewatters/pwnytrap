##
# PwnyTrap
#
# Created by David Watters 2021
# https://github.com/davewatters
#
# PwnyTrap queries the HaveIBeenPwned.com API to determine
# if a given password or email address
# has been compromised in a data breach.
#
# The HIBP database and API were created by Troy Hunt and
# licensed under the Creative Commons Attribution 4.0
# International Licence
# https://troyhunt.com ; https://haveibeenpwned.com
#
# Python3, HIBP API v3
##
import textwrap
import json
import hashlib
import requests
import getpass
import re


APP_VERSION = 'PwnyTrap v1.0'
CREDS_FILE = 'creds.json'
HIBP_PWD_API_URL = 'https://api.pwnedpasswords.com/range/'
HIBP_API_URL = 'https://haveibeenpwned.com/api/v3/'
USER_AGENT = {"user-agent": "PwnyTrap"}


# This regex includes an apostrophe before the @
# as they are used in Irish email addresses
REGEX_EMAIL = r"^[a-zA-Z0-9._%'+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


# TODO Implement text colours


def cls():
    '''
    Clears the screen and places cursor at top left
    Similar to 'nix terminal clear or Win command cls
    '''
    print("\033[H\033[J", end="")
    print('123456789+' * 8)  # 123456789+123456789+
    return


def get_yesno(question="Yes or No?", def_opt=True):
    '''
    Gets user's response to a Yes or No question.
    Defaults to True for Yes if Enter key hit.
    '''
    if def_opt is None:
        option = ' [y/n] '
    elif not def_opt:
        option = ' [y/N] '
    else:
        option = ' [Y/n] '

    print("")
    while True:
        opt = input(question + option).strip()
        if opt == '':  # enter hit, empty input
            if def_opt is not None:
                reply = def_opt
                break
            else:
                print("You must choose a Yes or No option.")
                print("Valid options are 'Y'/'y' or 'N'/'n'.\n" +
                      "Please try again.\n")
                continue
        elif opt[0] in 'Yy':
            reply = True
            break
        elif opt[0] in 'Nn':
            reply = False
            break
        else:
            print(f"{opt} is not a valid option.")
            print("Valid options are 'Y'/'y' or 'N'/'n'.\n" +
                  "Please try again.\n")
            continue

    return reply


def disp_main_page():
    '''
    Displays the main greeting and menu options
    '''
    cls()
    s = f"""
        {APP_VERSION}\n
        -= Catch bad pa$$words using the Have I Been Pwned API =-\n\n
        App Mode Options:\n
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
    s = f"""
        {APP_VERSION} Help\n

        Lots of helpful info goes here.\n
        TODO explain checking passowrd pwnage
        TODO explain checking email address pwnage\n
        TODO Explain the HIBP API\n
        TODO Include a link to the HIBP site and also it's FAQ page\n

        Finally, in case you were wondering...
        PwnyTrap is pronounced 'Pony Trap'.  It comes from the
        leetspeak word 'pwn' meaning to be beaten or compromised
        in some way. For an explanation check this link:
        https://en.wikipedia.org/wiki/PWN\n
    """
    print(textwrap.dedent(s))
    input("Enter to return to the main screen..")
    return


class HibpAPI:
    '''
    Class to process data from the HIBP API
    API Services available are: breachedaccount, breaches, breach,
        dataclass, pasteaccount
    '''
    def __init__(self):
        self.api_url = HIBP_API_URL
        self.pwd_api_url = HIBP_PWD_API_URL
        self.user_agent = USER_AGENT

        # 
        # MOve to get_api_key method with
        # try/except error checking for
        # missing creds file, invalid key, expired key
        # 
        with open(CREDS_FILE) as f:
            self.api_key = json.load(f)

    def query_api(self, service_param):
        '''
        Queries the HIBP API using HTTP GET request to url.
        Accepts string containing api service with parameter.
        Returns requests Response object.
        '''
        url = self.api_url + service_param
        headers = {**self.api_key, **self.user_agent}
        return requests.get(url, headers=headers)

    def check_breached(self, email):
        '''
        Checks if email is in breach database.
        Accepts email address to check.
        Returns True|False if email is found in database.
        '''
        breached = False
        resp = self.query_api("breachedaccount/" + email)
        if resp.status_code == 200:
            breached = True
            # TODO display red text
            print("\nBad news - you've been pwned!")
            print("The password used with this account for any " +
                  "of the following services\n" +
                  "should be changed everywhere that it was used.")
            breaches = resp.json()
            # breaches is now a list of dicts
            print("\nEmail address appears in the following " +
                  f"{len(breaches)} data breaches..")
            for breach in breaches:
                print(breach['Name'])
        elif resp.status_code == 404:
            # TODO display green text
            print("\nGood news! Email address not found in breach data.")
        else:
            print(f"Response code: {resp.status_code}")
            print("Error calling API")
            print("Should be an exception handling block here")
        return breached

    def check_passwd(self, password):
        passwd_hash = hashlib.sha1(password.encode('utf-8')).hexdigest()
        print('\nPassword encrypted')
        print(f'SHA-1 hash digest of password: {passwd_hash}')
        search_hash = passwd_hash[:5].upper()
        resp = requests.get(HIBP_PWD_API_URL + search_hash)
        matches = resp.text.splitlines()
        count = 0
        for s in matches:
            h, c = s.split(':')
            if search_hash + h == passwd_hash.upper():
                count = int(c)
                break

        if count > 0:
            # TODO display red text
            print("\nBad news - you've been pwned!")
            print(f"Password appeared {count:,} times in the database.")
            print("This password should never be used again.")
        else:
            # TODO display green text
            print("\nGood news! Password not found in database.")
            print("Remember, this does NOT mean that it is a GOOD password," +
                  "\njust that it hasn't yet appeared in an online dump.")

        return

    def show_all_breaches(self):
        '''
        Show the full list of breaches currently in the HIBP dump
        '''
        resp = self.query_api("breaches")
        breaches = resp.json()
        for breach in breaches:
            print(f"{breach['Name'].strip():<40}", end='')

        get_yesno()
        return



def check_email():
    '''
    Accepts user input for email account to check
    Checks email for inclusion in HIBP breached accounts database
    '''
    print('\nChecking email address...')
    hibp = HibpAPI()
    email_regex = re.compile(REGEX_EMAIL)
    while True:
        email = input("\nEnter email account to check: ")
        if not email_regex.search(email):
            print(f"\n{email} doesn't appear to be a valid email address.")
            print("Please try again.")
            continue
        else:
            hibp.check_breached(email)

        if not get_yesno("Check another?"):
            break
    return


def check_password():
    '''
    Accepts user input for password to check
    Checks password for inclusion in HIBP breached passwords database
    '''
    while True:
        print('\nChecking password...\n')
        print("* Only partial SHA-1 hash of password will be used")
        print("* Password will not be logged or sent over the internet\n")
        passwd = getpass.getpass('Enter password to check: ')

        HibpAPI().check_passwd(passwd)

        if not get_yesno("Check another?"):
            break
    return


def main():
    '''
    Main program loop
    '''
    disp_main_page()
    while True:
        opt = input("Enter your choice [1-4, or q to quit]: ")
        if (len(opt) != 1) or (opt not in "1234q"):
            print(f"\n{opt} is not a valid option. Valid options " +
                  "are 1, 2, 3, 4 or q.\nPlease try again.\n")
            continue
        elif opt == 'q':
            print('Goodbye.')
            break
        elif opt == '1':
            help_screen()
        elif opt == '2':
            check_password()
        elif opt == '3':
            check_email()
        elif opt == '4':
            HibpAPI().show_all_breaches()
        disp_main_page()


##
main()
##
