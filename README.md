# PwnyTrap

## A Python App to let you check whether a password or an email address has been compromised and is in the [HaveIBeenPwned.com](https://haveibeenpwned.com) breach database.
<br />

You can view the PwnyTrap live app [HERE.](https://ci-wp3-love-sandwiches.herokuapp.com/)
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
[ This app was created as the third Portfolio Project (PP3) for the Code Institute's Full Stack Web Development course. As a requirement for a portfolio project the app is deployed to showcase Python skills.]  

PwnyTrap's purpose is to query the HaveIBeenPwned API to see if a given password or email address was compromised in a data breach.  If a password is present then that password must never be used again as it much more likely to be susceptible to a credential stuffing attack.  Similarly, if an email account is identified in a particular breach, then anywhere its accompanying password was used must be changed and never used again.

I see potential for this Python tool to be used in a number of ways:

1. in end-user training to encourage people to adopt better password practises
1. in software development to encourage security awareness and better coding practises 
1. to encourage it's inclusion as another security step in software when new logons are created or passwords are changed 
1. perhaps further developed to check existing Active Directory accounts or a company's email domain accounts for potential security vulnerabilities

#_TODO explain use of hashing so that password is never sent over network etc.  Or leave for Desgin / Features section?

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
        #_TODO

## - Features -
- #_TODO

## - Future Features -
- #_TODO

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
1. [Google Fonts:](https://fonts.google.com/)
    - Google font(s) were imported in the style.css file and used throughout the site.  
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used to add icons for aesthetic and UX purposes.   
1. [TinyPNG:](https://tinypng.com/)
    - tinypng.com was used to compress large images

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

-  Other projects using the HIBP API providing inspiration included:
    https://github.com/Radial01/PwnyCorral
    https://github.com/lionheart/pwnedpasswords  
    https://github.com/RubikX/HIBP-Python/


### Acknowledgements

-   My mentor [Daisy McGirr](https://github.com/Daisy-McG) for all her helpful feedback and knowledge.
-   The Code Institute community on Slack and the CI staff and students for their feedback and support.
