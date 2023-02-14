# PwnyTrap

### A Python tool to query the HaveIBeenPwned.com v3 API to see if a given password or email address has been compromised in a data breach.  

<!-- <h2 align="center"><img src="readme-docs/pwnytrap-v1.0-main-screen.png"></h2> -->

## Quick Links  
* [Purpose](#purpose)
* [Features](#features)
* [Requirements](#requirements)
* [Usage](#usage)
* [Bugs](#bugs)
* [Credits](#credits)

## Purpose      
PwnyTrap is Python command line tool to query the HaveIBeenPwned.com API to see if a given password or email address was compromised in a data breach.

PwnyTrap's primary purpose is to enable quick password & email address lookups to the HaveIBeenPwned.com (aka HIBP) database. Additionally, it was created with an idea in mind for a Python module which could be imported for use in future projects to enhance IT security, for example, during a user signup/registration process.  This concept of not allowing breached password reuse is discussed in detail in [Troy Hunt's blog post](https://www.troyhunt.com/introducing-306-million-freely-downloadable-pwned-passwords/) written after the release of the updated [NIST Digital Identity Guidelines (SP 800-63)](https://www.nist.gov/special-publication-800-63). In these updated guidelines NIST specifically recommend that users' passwords are checked against those found in data breaches so that they can not be reused.


## Features    

- **Check Password:** The input value is immediately SHA-1 hashed. For security, the entered plaintext value of the password is never used - it never leaves the machine or is saved anywhere.  PwnyTrap takes only the first five characters of the hash to build the search query for the API. This API 'range search' returns multiple hash suffixes which help preserve the anonymity of the user. This is possible by HIBP implementing [password privacy using the **_k-Anonymity model_.**](https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/#cloudflareprivacyandkanonymity)  
     

- **Check Email Address** requires a valid [HaveIBeenPwned.com API Key](https://haveibeenpwned.com/API/Key). Input is then checked to ensure that a valid email address was entered.  Note that this does _not_ check if it is a _live_, or active, email account, only that a _correctly formatted_ email address was entered.

- **Show All Breaches** returns all 500+ breach names in the HIBP database.

- **Lookup Breach Info** allows the user to enter a breach name and call up full details of the breach including a description and the details of types of data exposed in the breach.


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
Download `pwnytrap.py`.  If you registered for an API key from HIBP, create the `creds.json` in the same folder.  
Basic usage is 
```
python3 pwnytrap.py [ -p|-e <email_address> ]
```

or if you create an aliased wrapper script 
```
hibp [ -p|-e <email_address> ]
```
It can be helpful to create a small wrapper script and deploy it as `~/bin/pwnytrap.sh`. Edit `PWNY_DIR` on line 2 to point to wherever you out PwnyTrap. Finally, `alias hibp='pwnytrap.sh $1 $2'`.
```
#!/usr/bin/env bash
PWNY_DIR=~/dev/pwnytrap/
last_wd=${pwd}
cd ${PWNY_DIR}
python3 ${PWNY_DIR}pwnytrap.py $1 $2
cd ${last_wd}
```


## Bugs  
- None reported

## Future Features
-   Refactor as a Django password validator plugin
-   Refactor the HibpAPI class to search on NTLM hashes (aka NTHash) of the given password.  Create an option or separate Active Directory test tool using HIBP's offline NTLM hash dump.
-   Create an option (or new tool) to scan a company's whole email domain for accounts exposed in a breach 


## Credits 

### Author
David Watters / [@GitHub](https://github.com/davewatters) / [@LinkedIn]()

### Acknowledgements
-   The [HaveIBeenPwned API](https://haveibeenpwned.com/API/v3) was created by [Troy Hunt](https:/troyhunt.com) and is licensed under the [Creative Commons Attribution 4.0 International Licence](https://creativecommons.org/licenses/by/4.0/)

-   Full HIBP API v3 Specification Document [HERE](https://haveibeenpwned.com/API/v3)
### See Also

-   [NIST Digital Identity Guidelines (SP 800-63)](https://www.nist.gov/special-publication-800-63)
-   Futher reading about implementing password privacy using the **_k-Anonymity model_**  
    https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/#cloudflareprivacyandkanonymity 

    https://blog.cloudflare.com/validating-leaked-passwords-with-k-anonymity/
-   Other projects using the HIBP API providing inspiration included:  
    https://github.com/Radial01/PwnyCorral  
    https://github.com/lionheart/pwnedpasswords    
    https://github.com/RubikX/HIBP-Python/  
-   A shout out to https://pythex.org which was used to test the regular expressions. 

- Version 1.0 of this tool was originally created as [my third Portfolio Project](https://github.com/davewatters/pwnytrap-ci-pp3) for the Code Institute's Full Stack Web Development course.
