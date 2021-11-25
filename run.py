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
import getpass
import hashlib
import json
import re
import requests
import textwrap

from pprint import pprint


APP_VERSION = 'PwnyTrap v1.0'
CREDS_FILE = 'creds.json'
HIBP_API_URL = 'https://haveibeenpwned.com/api/v3/'
HIBP_PWD_API_URL = 'https://api.pwnedpasswords.com/range/'
USER_AGENT = {"user-agent": "PwnyTrap"}


# Email regex includes an apostrophe before the @ symbol -
# they are used in Irish email addresses (common surnames)
REGEX_EMAIL = r"^[a-zA-Z0-9._%'+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
REGEX_HTML = r"<[^<]+?>"


# TODO Implement text colours


def cls():
    '''
    Clears the screen and places cursor at top left
    Similar to 'nix terminal clear or Win command cls
    '''
    print("\033[H\033[J", end="")
    print('123456789+' * 8)  # 123456789+123456789+
    return


def get_yesno(question='', def_opt=True):
    '''
    Gets user's response to a Yes or No question.
    Optional parameter Defaults to True for Yes if Enter key hit.
    Returns True|False if Yes|No is chosen
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


def strip_html(str):
    '''
    Strip HTML markup tags from passed in string.
    Returns stripped text string.
    '''
    html_regex = re.compile(REGEX_HTML)
    stripped = html_regex.sub('', str)
    return stripped


def disp_main_page():
    '''
    Displays the main greeting and menu options
    '''
    cls()
    s = f"""
        {APP_VERSION}\n
        -= Catch bad pa$$words using the Have I Been Pwned API =-\n\n
        App Mode Options:\n
        0. Show Help screen\n
        1. Check password\n
        2. Check email address\n
        3. Lookup breach details\n
        4. Show all breaches\n
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
    API Services implemented: breachedaccount, breaches, breach
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
            # TODO
            print("Should be an exception handling block here") # TODO

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
            # s contains '<--35 char hash suffix-->:<count>'
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
        breaches = resp.json()  # returns a list of dicts
        col = 0
        for breach in breaches:
            # for each outer loop I'd like three columns
            if col < 3:
                print(f"{breach['Name'].strip():<26}", end='')
                col += 1
            else:
                print("")
                col = 0

        print(f"\nThere are {len(breaches)} breaches listed.")
        print("\nYou can use the breach name as it appears in this list\n" +
              "with the Lookup Breach Details menu option.")

        while True:
            if get_yesno("Return to main menu?", False):
                break
        return

    def breach_details(self, name=''):
        '''
        Retrieve & display details record of a particular breach.
        Accepts the breach name to search for, defaults to empty str.
        If no breach passed in, prompts the user to enter one.
        '''
        while True:
            if name == '':
                # ask the user to enter a search term
                name = input("\nEnter breach name: ").strip().replace(' ', '')

            resp = self.query_api("breach/" + name)
            if resp.status_code == 200:
                breach = resp.json()
                self.disp_breach_details(breach)

            elif resp.status_code == 404:
                print(f"\nBreach name {name} not found.")
        
            if get_yesno("Search for another breach?"):
                name = ''
                continue
            else:
                break
        return

    def disp_breach_details(self, breach):
        '''
        Displays the breach details on screen. Accepts breach dictionary.
        Iterates dict, formatting or skipping certain vaules.
        '''
        dont_display = [
            'AddedDate',
            'IsRetired',
            'IsSensitive',
            'LogoPath',
            'ModifiedDate'
        ]
        print('')
        for k, v in breach.items():
            if k in dont_display:
                continue
            elif k == 'PwnCount':
                print(f"Number of Compromised Accounts: {v:,}")
            elif k == 'Description':
                print(f"{k:12}:\n{strip_html(v)}")
            elif k == 'DataClasses':
                print(f"Type of Data Compromised:\n    {v}")
            else:
                print(f"{k:12}: {v}")

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
    Main program loop.
    Displays the main screen and menu control loop.
    '''
    disp_main_page()
    while True:
        opt = input("Enter your choice [0-4, or q to quit]: ")
        if (len(opt) != 1) or (opt not in "01234q"):
            print(f"\n{opt} is not a valid option. Valid options " +
                  "are 0, 1, 2, 3, 4 or q.\nPlease try again.\n")
            continue
        elif opt == 'q':
            print('Goodbye.')
            break
        elif opt == '0':
            help_screen()
        elif opt == '1':
            check_password()
        elif opt == '2':
            check_email()
        elif opt == '3':
            HibpAPI().breach_details()
        elif opt == '4':
            HibpAPI().show_all_breaches()

        disp_main_page()


##
main()
##
