# README

## Installation
1. Create a virtual environment:
``` python3 -m venv venv```
2. Activate virtual environment:
``` source venv/bin/activate ```
3. In the virtual environment, install flask:
```pip install flask```

4. Initialize an empty database with 2 posts, 1 normal user, 1 admin:
```python3 init_db.py```

5. Start the flask app:
```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

_Note: For Windows:_
2. _Activating virtual environments might work with ```.\venv\Scripts\activate```_
5. _Start the app with:_
```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

6. After you have initialized the database, you can use 2 default users:
| user | password | is admin |
|----------|----------|----------|
| maija| kissa | no |
| admin | admin | yes |

## Usage
Server runs on http://127.0.0.1:5000/

Navigate to the page in your browser and test it out with the accounts above (see 6).


## Credits and information:
This application was created as coursework for a Cyber Security Course project at University of Helsinki.
The information about the course can be found here: 
https://cybersecuritybase.mooc.fi/module-3.1 

Basic functionalities are from these tutorials: 
https://www.digitalocean.com/community/tutorials/

Additional information on vulnerable web apps from this course: https://hy-tsoha.github.io/materiaali/osa-4/#tietoturva 
