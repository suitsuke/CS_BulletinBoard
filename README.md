# Start
Activate virtual environment:
source venv/bin/activate

To initialize an empty database with 2 blog posts, 1 normal user, 1 admin:
python3 init_db.py

export FLASK_APP=app
export FLASK_ENV=development
flask run

For testing:
After you have initialized the database, you can use 2 default users:
user / password / is admin
maija / kissa / no
admin / admin / yes

Server runs on http://127.0.0.1:5000/
Navigate to the page in your browser and test it out.


Basic functionalities from this tutorial https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application 