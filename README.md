# Start
Activate virtual environment:
source venv/bin/activate

To initialize an empty database with 2 blog posts:
python init_db.py

export FLASK_APP=app
export FLASK_ENV=development
flask --debug run


Basic functionalities from https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application 