import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort, make_response
#hash password to not store it in plaintext
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def is_logged_in():
    return "username" in request.cookies and request.cookies["username"] != ""

def is_admin_user():
    #should return true or false
    #look at database for the current logged in user
    if "username" not in request.cookies:
        return False  # User is not logged in, so not an admin

    username = request.cookies["username"]

    conn = get_db_connection()
    result = conn.execute('SELECT admin FROM users WHERE username = ?', (username,))
    user = result.fetchone()
    conn.close()

    if user is None:
        return False  # User does not exist in the database, so not an admin

    return user['admin'] == 1

@app.route('/')
def index():
    
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    # Generate HTML content for each post
    posts_html = ""
    for post in posts:
        post_html = """
        <div class='post'>
            <p>{}</p>
            <h2>{}</h2>
            <p>{}</p>
            {}
        </div>
        """.format(post['created'], post['title'], post['content'], '<a href="/{}/edit">Edit</a>'.format(post['id']) if is_admin_user() else '')
        posts_html += post_html

    # Final HTML content including all posts
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Posts - FlaskApp</title>
    </head>
    <body>
        <nav>
        <span style="font-size: 3em; color: #d64161; margin-left: 50px; text-decoration: none;">
            <a href="/">Guestbook</a>
            <a href="/create">Write</a>
            <a href="/login_page">Login</a>
        </span>
        </nav>
        <hr>
        <div class="content">
            {}
        </div>
    </body>
    </html>
    """.format(posts_html)

    return html_content


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if not is_logged_in():
        return redirect(url_for('login_page'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            pass
        elif not content:
            pass
        else:
            conn = get_db_connection()
            sql = "INSERT INTO posts (title, content) VALUES ('" + title + "', '" + content + "')"
            conn.execute(sql)
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    if not is_logged_in():
        return redirect(url_for('login_page'))

    if not is_admin_user():
        return redirect(url_for('index'))

    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            pass

        elif not content:
            pass

        else:
            conn = get_db_connection()
            sql = 'UPDATE posts SET title = \'' + title + '\', content = \'' + content + '\' WHERE id = ' + str(id)
            conn.execute(sql)
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = {}'.format(id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Check username and password
    sql = "SELECT id, password FROM users WHERE username=:username"
    conn = get_db_connection()
    result = conn.execute(sql, {"username": username})
    user = result.fetchone()

    if not user:
        return redirect("/login_page")
    else:
        user_id, hash_value = user  # Unpack the user tuple

    if check_password_hash(hash_value, password):
        # Set a cookie with the username
        response = make_response(redirect("/"))
        response.set_cookie("username", username)

        return response
    else:
        return redirect("/login_page")


@app.route("/logout")
def logout():
    # Delete the username cookie
    response = make_response(redirect("/"))
    response.set_cookie("username", "", expires=0)
    return response


@app.route('/login_page/')
def login_page():
    return render_template('login_page.html')