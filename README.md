# How to run this project?


A. Make sure you have installed-

	1. python
	2. Django 

on your device. 

B. Check if you have installed python and django properly using these commands:

	 python --version
	 pip --version
	 python -m django --version

C. If not installed, follow these steps:

	1. Go to 'https://www.python.org/downloads/' then download and install python.
	2. Install python, then open terminal and run 'python get-pip.py' to install pip
	2. Install python, then open terminal and run 'pip install django' to install latest version of django


D. To run project follow these steps:

	1. extract ParkingBDv2.rar
	2. go to extracted folder
	3. open gitBash/terminal at the directory where "manage.py" file exists.
	4. run these commands: 
		py -m venv env
		source env/Scripts/activate
		pip install -r requirements.txt
		py manage.py runserver
	5. go to link:
		 http://localhost:8000/
	6. To run livereload, run this on another gitBash/terminal(optional)-
		source env/Scripts/activate
		py manage.py livereload
        

# Registration-and-login-system
This web app has been developed using the popular Django framework and Bootstrap for the frontend. My motivation to build this project is so that I can learn about Django and tighten up my skills. This mini-app can be easily integrated into a bigger system project that needs to have a registration and login system.

### Basic Features of The App
    
* Register – Users can register and create a new profile
* Login - Registered users can login using username and password
* Social Apps Login – Users can login using their GitHub or Google account
* User Profile - Once logged in, users can create and update additional information such as avatar and bio in the profile page
* Update Profile – Users can update their information such as username, email, password, avatar and bio
* Remember me – Cookie Option, users don’t have to provide credentials every time they hit the site
* Forgot Password – Users can easily retrieve their password if they forget it 
* Admin Panel – admin can CRUD users

### Quick Start
To get this project up and running locally on your computer follow the following steps.
1. Set up a python virtual environment
2. Run the following commands
```
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
   
3. Open a browser and go to http://localhost:8000/
