# auth_project
Simple authentication and login page. The program stores User information in a database and
hashes the password for future verification.

## Requirements:
* python 3.8
* flask
* flask_login
* flask_wtf
* flask_sqlalchemy

## Installation

1. Create a virtual environment in a folder of your choosing with the following command: 

`python3 -m venv your_venv_name_here`

2. Change folder to the newly created virtual environment with `cd your_venv_name_here`, clone the repository with the following command:

`git clone https://github.com/DJMaidana/auth_project`

3. Still inside the root folder, activate the virtual environment with:

`source bin/activate`

4. Change folder with `cd auth_project` and install the required dependencies with:

`pip install -r requirements.txt`

5. Execute the program with:

`flask run`

6. Ctrl+LeftClick the link the console provides you, or copy it in your internet explorer address bar to explore this project. 

# Future Work

Things to improve: 
* Add unit test 
* Add e-mail confirmation
* Multi-Factor Authentication
* Better UI-UX
