# PwnyTrap

### A Python tool to let you check whether a password or an email address has been compromised and is in the [HaveIBeenPwned.com](https://haveibeenpwned.com) breach database.
<br />

You can view the PwnyTrap live app [HERE.](https://ci-pp3-pwnytrap.herokuapp.com/)
<br />
<br />
<!-- Responsive desgin sample image from http://ami.responsivedesign.is/ -->
#_TODO Screen sample image goes here
<!-- <h2 align="center"><img src="readme-docs/ci-pp2-blackjack-responsive-mockup.png"></h2>
-->

## - Table of Contents -
* [Purpose](#purpose)
* [User Experience Design (UX)](#user-experience-design)
* [Features](#features)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## - Purpose -
[ This app was created as the third Portfolio Project (PP3) for the Code Institute's Full Stack Web Development course. As a requirement for a portfolio project the app is to showcase Python skills and is deployed in the Code Institute mock terminal on Heroku.]  

In short:  
A Python tool to query the HaveIBeenPwned API to see if a given password or email address was compromised in a data breach.

In more detail:   
PwnyTrap's purpose is to query the HaveIBeenPwned API to see if a given password or email address was compromised in a data breach.  If a password is present then that password must never be used again as it much more likely to be susceptible to a [credential stuffing](https://owasp.org/www-community/attacks/Credential_stuffing) attack.  Similarly, if an email account is identified in a particular breach, then its accompanying password must be changed and never used again for any service.

The primary audience for this tool would appear to be the IT professional, but it is in fact for *all* online users, as its ultimate purpose is to educate and raise awareness about taking the security of our online identity seriously.  For SysAdmins & Tech Support there is an obvious and immediate benefit to having a quick command-line tool to check if an email address or password has been compromised.  

Additionally, for software developers there is a need to encourage awareness around designing software with security in mind.  This app could be integrated into a website registration form to inform the user of a previous breach at point of entry so that a better decision can be made when choosing a password.  

As internet users, people are creatures of habit and for convenience will often reuse the same password across multiple sites.  If a trusted IT service professional shows the user their results from the HIBP search it can encourage them to rethink how they approach their online security.  

It's important to note that the entered password is never sent over the network or logged by the program.

## - User Experience Design -

-   ### User stories

    -   ### Design Strategy Goals
        -    #_TODO

    -   ### Design Scope to Deliver MVP
        -   #### First Time Visitor Goals
            As a first time user...
            -  #_TODO

        -   #### Returning Visitor Goals
            As a returning visitor...
            -   #_TODO

        -   #### Frequent User Goals
            As a frequent user...
            -   #_TODO


-   ### Design
    -   #### Layout
        The program is designed as a command-line app and to run in the Code Institute project terminal on Heroku.  The default maximum terminal screen width is 80 characters and default height is 24 characters. The terminal window will automatically scroll up.   

## - Features -
- #_TODO  
    Password privacy using the [k-anonymity model](https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/#cloudflareprivacyandkanonymity)


## - Future Features -
- #_TODO
-   Check Active Directory accounts passowrds using the offline NTLM hash download
-   Scan a company's whole domain email accounts exposure in a breach
<!--  -->
<!-- End Features -->
<!--  -->


## - Technologies Used -

### Languages Used

-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Git](https://git-scm.com/)
    - Git was used for version control and managed via the VSCode terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git, and Github Pages used to deploy the live site
1. [Heroku](https://heroku.com)
    - Heroku was used to deploy the app using a Code Institute template
<!---  --->
<!---  Begin testing section --->
<!---  --->

## - Testing -


### Code Validation
The [PEP8 Online](http://pep8online.com) was used

- #_TODO


### Bugs

1. #_TODO

<!---  --->
<!--- end of testing section --->
<!---  --->

## - Deployment -

### Heroku  
The live deployed site can be viewed on Heroku [HERE](https://ci-pp3-pwnytrap.herokuapp.com)

The Project repository (repo) is at [https://github.com/davewatters/pwnytrap](https://github.com/davewatters/pwnytrap)

Note: The project repo was initially generated from the [Code Institute Python Essentials template](https://github.com/Code-Institute-Org/python-essentials-template) 

Deployment of the site to Heroku was done as follows:
 
1.  Login to your Heroku account
1.  Create a New App
1.  (Important!) Select the 'Settings' tab first
1.  Click on 'Reveal Config Vars'
1.  Add any relevant config vars by entering the KEY/VALUE pair data, e.g. PORT & 8000
1.  Select 'Add Buildpack'
1.  (Important!) Select Python first, then select NodeJS
1.  Select the 'Deploy' tab
1.  For the Deplyoment Method select GitHub
1.  Connect to GitHub repo by entering YOUR-REPO-NAME, then Connect
1.  A message will confirm that your app was successfuly deployed
1.  Test that the site has successfully gone live by clicking on the 'View' button
1.  Your app can now be accessed via any browser at: `https://YOUR-APP-NAME.heroku.com`


## - Credits - 

-   Project inspired by [Troy Hunt's](https:/troyhunt.com) [Have I Been Pwned](https://haveibeenpwned.com) website
-   Full HIBP API v3 Specification Document [HERE](https://haveibeenpwned.com/API/v3)

### Code
-   No code was directly copied to this project but numerous resources helped me understand what I needed and how best to code it. These include: The official [Python Docs](https://docs.python.org), StackOverflow.com, W3Schools.com, RealPython.com  
-   Automate the Boring Stuff with Python, 2nd Edition - Al Sweigart. Very helpful as an intro to implementing regex searching in Python and also working with the requests and json modules
-   https://www.regular-expressions.info/email.html
-   Other projects using the HIBP API providing inspiration included:  
    https://github.com/Radial01/PwnyCorral  
    https://github.com/lionheart/pwnedpasswords    
    https://github.com/RubikX/HIBP-Python/  


### Acknowledgements

-   The HIBP database and API were created by Troy Hunt and licensed under the Creative Commons Attribution 4.0 International Licence
-   My mentor [Daisy McGirr](https://github.com/Daisy-McG) for all her helpful feedback and knowledge.
-   The Code Institute community on Slack and the CI staff and students for their feedback and support.
