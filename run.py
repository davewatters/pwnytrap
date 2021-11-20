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


def cls():
    '''
    Clears the screen and places cursor at top left
    Similar to *nix terminal clear or Win cls
    '''
    print("\033[H\033[J", end="")
    print('123456789+' * 8)
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
        TODO explain checking passowrd pwnage\n
        TODO explain checking email address pwnage\n\n
        TODO Explain the HIBP API\n
        TODO Include a link to the HIBP site and also it's FAQ page\n

        Finally, in case you were wondering...\n
        PwnyTrap is pronounced 'Pony Trap'.  It comes from the leetspeak word 'pwn' meaning to be beaten or compromised in some way. 
        For an explanation check this link: https://en.wikipedia.org/wiki/PWN\n
    """
    print(textwrap.dedent(s))
    input("Any key to return to the main screen...")
    return


def main():
    '''
    Main program loop
    '''
    while True:
        disp_main_page()
        opt = input("Enter your choice [1-4, or 0 to quit]: ")
        if opt == '0' or opt == 'q':
            print('Goodbye.')
            break
        elif opt == '1':
            help_screen()


##
main()
##
