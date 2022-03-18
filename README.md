# PwnyTrap

### A Python tool to query the [HaveIBeenPwned.com](https://haveibeenpwned.com) API to see if a given password or email address has been compromised in a data breach.  

<!-- <h2 align="center"><img src="readme-docs/pwnytrap-v1.0-main-screen.png"></h2> -->

## Table of Contents  
* [Purpose](#purpose)
* [Features](#features)
* [Requirements](#requirements)
* [Usage](#usage)
* [Future Features and Bugs](#future-features-and-bugs)
* [Deployment](#deployment)
* [Credits](#credits)

## Purpose      
PwnyTrap is Python cmd line tool to query the HaveIBeenPwned.com API to see if a given password or email address was compromised in a data breach.

PwnyTrap's purpose on one level is to be a simple tool to easily enable password & email address lookups to the HaveIBeenPwned.com (aka HIBP) database. On another level, it was created as an idea for a Python module which could be imported for use in future projects to enhance IT security, for example, during a user signup/registration process.


## Features    

- **Check Password** The password is SHA-1 hashed then only the first five characters are used to build the search query for the API. This API 'range search' returns multiple hash suffixes to preserve the anonymity of the user. (You can read more about implementing password privacy using the _k-Anonymity model_ [here](https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/#cloudflareprivacyandkanonymity).) 


- **Check Email Address** allows the user to type in an email address. The input is checked to ensure that a valid, i.e. a _correctly formatted_, email address was entered (does _not_ check if it is a live email account)

- **Lookup Breach Info** allows the user to enter a breach name and call up full details of the breach including a description and the details of types of data exposed in the breach.

- **Show All Breaches** returns all 500+ breach names in the HIBP database.


## Requirements 
- Python 3.6+  
- The following dependencies are required:
    ```
    pip install requests
    ```
- HIBP v3 API Key  
    To search for compromised **email addresses** this app requires a valid [HaveIBeenPwned.com API Key](https://haveibeenpwned.com/API/Key).  When the program is run it checks for the key in a file called `creds.json`, which has the following format:
    ```
    {
      "hibp-api-key": "[_SECRET_API_KEY_]"
    }
    ```
    Note that this key is not required for password searches.  

## Usage  
See [Deployment](#deployment) below for details of creating a helpful wrapper script, otherwise basic usage is: 
```
python3 pwnytrap.py [ -p|-e <email_address> ]
```

## Future Features and Bugs  

### Future Features
-   Refactor the HibpAPI class to search on NTLM hashes (aka NTHash) of the given password.  Create an option or separate Active Directory test tool using HIBP's offline NTLM hash dump.
-   Create an option (or new tool) to scan a company's whole email domain for accounts exposed in a breach 


### Bugs  

1. None known at this time


## Deployment

Use Vim to create a small wrapper script and deploy to `~/bin/pwnytrap.sh`. 
```
#!/usr/bin/env bash
PWNY_DIR=~/dev/pwnytrap/
last_wd=${pwd}
cd ${PWNY_DIR}
python3 ${PWNY_DIR}pwnytrap.py $1 $2
cd ${last_wd}
```
Just edit `PWNY_DIR` on line 2 to point to wherever you put your copy of `pwnytrap.py` and the `creds.json` files. Finally, `alias pwnytrap='pwnytrap.sh $1 $2'`.


## Credits 

Full details available at the GitHub Project repo:  [https://github.com/davewatters/pwnytrap](https://github.com/davewatters/pwnytrap)
-   Project inspired by [Troy Hunt's](https:/troyhunt.com) [Have I Been Pwned](https://haveibeenpwned.com) website
-   Full HIBP API v3 Specification Document [HERE](https://haveibeenpwned.com/API/v3)

-   A shout out to **https://pythex.org** which was used to test the regular expressions used. 

-   Other projects using the HIBP API providing inspiration included:  
    https://github.com/Radial01/PwnyCorral  
    https://github.com/lionheart/pwnedpasswords    
    https://github.com/RubikX/HIBP-Python/  


### Acknowledgements

-   The HIBP API was created by [Troy Hunt](https:/troyhunt.com) and is licensed under the [Creative Commons Attribution 4.0 International Licence](https://creativecommons.org/licenses/by/4.0/)

- This app was originally created as the third Portfolio Project (PP3) for the Code Institute's Full Stack Web Development course. The app was to showcase Python skills, and as a requirement was deployed to Heroku using a Code Institute mock terminal template.]  