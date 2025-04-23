# Berriest Blues by The Bluest Berries

## Roster
* Leon Huang
* Amanda Tan
* Jason Chao
* Nia Lam

## App Description/Summary
Our aim is to create a website that can visually demonstrate and display correlations between student performance and various factors based on our dataset. Specifically, users may look at attendance, study hours, sleep hours, and tutoring data per student. In order to visualize the data, we will utilize Chart.js to allow the user to generate graphs and charts. 

# Install Guide

**Prerequisites**

Ensure that **Git** and **Python** are installed on your machine. It is recommended that you use a virtual machine when running this project to avoid any possible conflicts. For help, refer to the following documentation:
   1. Installing Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git 
   2. Installing Python: https://www.python.org/downloads/ 

   3. (Optional) Setting up Git with SSH (Ms. Novillo's APCSA Guide): https://novillo-cs.github.io/apcsa/tools/ 
         

**Cloning the Project**
1. Create Python virtual environment:

```
$ python3 -m PATH/TO/venv_name
```

2. Activate virtual environment 

   - Linux: `$ . PATH/TO/venv_name/bin/activate`
   - Windows (PowerShell): `> . .\PATH\TO\venv_name\Scripts\activate`
   - Windows (Command Prompt): `>PATH\TO\venv_name\Scripts\activate`
   - macOS: `$ source PATH/TO/venv_name/bin/activate`

   *Notes*

   - If successful, command line will display name of virtual environment: `(venv_name) $ `

   - To close a virtual environment, simply type `$ deactivate` in the terminal


3. In terminal, clone the repository to your local machine: 

HTTPS METHOD (Recommended)

```
$ https://github.com/leonhuang12/the_bluest_berries__leonh15_amandat109_jasonc573_nial24.git
```

SSH METHOD (Requires SSH Key to be set up):

```
$ git@github.com:leonhuang12/the_bluest_berries__leonh15_amandat109_jasonc573_nial24.git
```

4. Navigate to project directory

```
$ cd PATH/TO/the_bluest_berries__leonh15_amandat109_jasonc573_nial24/
```

5. Install dependencies

```
$ pip install -r requirements.txt
```
        
# Launch Codes

1. Navigate to project directory:

```
$ cd PATH/TO/the_bluest_berries__leonh15_amandat109_jasonc573_nial24/
```
 
2. Navigate to 'app' directory

```
 $ cd app/
```

3. Run App

```
 $ python3 __init__.py
```
4. Open the link that appears in the terminal to be brought to the website
    - You can visit the link via several methods:
        - Control + Clicking on the link
        - Typing/Pasting http://127.0.0.1:5000 in any browser
    - To close the app, press control + C when in the terminal

```    
* Running on http://127.0.0.1:5000
``` 


### FEATURE SPOTLIGHT
- HTML indication current page
- Theme consistency with blue site, and round buttons mathcing the blue berries theme
- Viewablility: wide chart and for easy viewing
- Security: bcrypt for safe passwords
- Topic Relevancy: grades for stuy students

### KNOWN BUGS/ISSUES
- Droplet hosting: Internal Server Error
- Inaccessible to non registered users
- Unutilized database field (non integer, not relevant)
- Database Connectivity: Mongodb approving IP addresses before permissing connections
