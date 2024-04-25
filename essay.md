# Essay

## LINK: [link to the repository](https://github.com/suitsuke/CS_BulletinBoard/tree/vulnerable)

This project on github has a master branch which is a fixed, secure working app. The vulnerable branch is linked above. The vulnerable branch includes the flaws listed below, and the fixes for the flaws will be in the master branch. All fixes and flaws are permalinks in the essay. This essay can also be read on github with markdown formatting: 
Installation instructions are found in the README.md
In short, initialize the database and run the server.

For the essay, I am using OWASP 2017 Top 10 and CSRF, which is a fundamental flaw allowed in the project instructions.

## FLAW 1: A6:2017-Security Misconfiguration

[Line 26 in init_db.py](https://github.com/suitsuke/CS_BulletinBoard/blob/99919fac98469bf3e8f4129935dfd7b02669d64c/init_db.py#L26)

There is a security misconfiguration by using a default configuration for the admin password, which is admin. Anyone can log in with username admin and password admin, and delete everything that has been posted on the public bulletin board.

This application doesn't provide the user a way to change their password, so the editing should be done manually. This can be done when initializing the database at the start, and editing the highlighted line with something more secure, that is not a default password. A secure password should be long, include upper- and lowercase letters, special characters and numbers. Something a bit more secure could be, e.g., Secur3Password#.
Add the new secure password to this line instead.

## FLAW 2: A3:2017-Sensitive Data Exposure

[Iniatilizing database in init_db.py](https://github.com/suitsuke/CS_BulletinBoard/blob/99919fac98469bf3e8f4129935dfd7b02669d64c/init_db.py#L26)

[Authenticating a user in the login function](https://github.com/suitsuke/CS_BulletinBoard/blob/99919fac98469bf3e8f4129935dfd7b02669d64c/app.py#L165)

Sensitive data, such as passwords, should be encrypted and not be handled or stored in plaintext. In this case the database is initialized and stores the users passwords in plaintext, as well as authenticating them by comparing the plaintext password from the database with the plaintext of the input from the user.

Fix it by hashing the passwords. In app.py, import the [werkzeug.security module](https://github.com/suitsuke/CS_BulletinBoard/blob/f49f0aebe0c7829bb26b2ef5c944a30b65e7f7de/app.py#L4C1-L4C74) which provides tools for checking and generating password hashes. For initializing the database, [hash the passwords.](https://github.com/suitsuke/CS_BulletinBoard/blob/f49f0aebe0c7829bb26b2ef5c944a30b65e7f7de/init_db.py#L25) For login, [check the password hash](https://github.com/suitsuke/CS_BulletinBoard/blob/f49f0aebe0c7829bb26b2ef5c944a30b65e7f7de/app.py#L142) and compare it with the the generated hash of the password from the database.

## FLAW 3: A1:2017-Injection

[In the create function](https://github.com/suitsuke/CS_BulletinBoard/blob/99919fac98469bf3e8f4129935dfd7b02669d64c/app.py#L102)

[and the edit function](https://github.com/suitsuke/CS_BulletinBoard/blob/99919fac98469bf3e8f4129935dfd7b02669d64c/app.py#L131)

[and the delete function.](https://github.com/suitsuke/CS_BulletinBoard/blob/99919fac98469bf3e8f4129935dfd7b02669d64c/app.py#L143)

If the user input is used in the database query as is, there is a possibility to manipulate the database. This can cause e.g. data manipulation, data loss, or data breach. As is, a malicious user could write a new post with the title "'; DROP TABLE posts; --" and anything in the textfield, which will render the whole database and thus the index page and the Bulletin Board unusable for anyone.

Fix this issue by using dynamical substitution with ? when accessing the database. Fixes with examples of this [here for create function](https://github.com/suitsuke/CS_BulletinBoard/blob/f49f0aebe0c7829bb26b2ef5c944a30b65e7f7de/app.py#L73), [here for the edit function](https://github.com/suitsuke/CS_BulletinBoard/blob/f49f0aebe0c7829bb26b2ef5c944a30b65e7f7de/app.py#L103) and [here for the delete function.](https://github.com/suitsuke/CS_BulletinBoard/blob/f49f0aebe0c7829bb26b2ef5c944a30b65e7f7de/app.py#L116)

## FLAW 4: A7:2017-Cross-Site Scripting (XSS)

[L47-84 in app.py](https://github.com/suitsuke/CS_BulletinBoard/blob/99919fac98469bf3e8f4129935dfd7b02669d64c/app.py#L47-L84)

XSS flaws happen when untrusted data supplied by a user is included on a webpage and rendered in HTML without validation or escaping. Attackers can execute scripts in browsers or redirect others to malicious sites. In this case any logged in user could write a post on the bulletin board, and include e.g. scripts
```<script>alert("You have been hacked!") </script>``` or format the text by supplying formatting in the title or content fields.

Fixing this flaw means that the user input should not be rendered as is, but rather escaped or protected by some other methods. Flask uses Jinja templating for creating dynamic content for webpages, and escaping content is a built in feature in Jinja. Thus we will create a new index function, and a separate index.html file which will have the new Jinja features built in to keep everything separate and improve the structure of the web app. [The new index-function](https://github.com/suitsuke/CS_BulletinBoard/blob/f49f0aebe0c7829bb26b2ef5c944a30b65e7f7de/app.py#L47-L54) will look like this, and simply render the page using the posts.
[In templates/index.html](https://github.com/suitsuke/CS_BulletinBoard/blob/f49f0aebe0c7829bb26b2ef5c944a30b65e7f7de/templates/index.html) the new page will display posts using Jinja methods, that have built-in escaping. The formatting is also inherited from the base.html template using Jinja methods. Escaping the user-submitted input before displaying it causes possible malicious code now to be displayed in plaintext instead of running it.

## FLAW 5: Cross Site Request Forgery (CSRF)

[Authenticating logged in user](https://github.com/suitsuke/CS_BulletinBoard/blob/99919fac98469bf3e8f4129935dfd7b02669d64c/app.py#L22)

[Authenticating admin user](https://github.com/suitsuke/CS_BulletinBoard/blob/99919fac98469bf3e8f4129935dfd7b02669d64c/app.py#L26-L29)

[Logging in a user with correct credentials](https://github.com/suitsuke/CS_BulletinBoard/blob/99919fac98469bf3e8f4129935dfd7b02669d64c/app.py#L168)

[Logging out a user](https://github.com/suitsuke/CS_BulletinBoard/blob/99919fac98469bf3e8f4129935dfd7b02669d64c/app.py#L179)

CSRF flaws happen when a web application doesn't authenticate that the request actually comes from the actual user. Since cookies work by storing a file on the user's computer, if they are not authenticated, anyone could edit their cookies to display the correct username and just pretend to be an admin or a logged in user without using a secret key.

To fix this, we will use the Flask sessions instead of just looking at the stored cookies. Flask sessions have built-in functionality for using a secret key and avoiding CSRF issues. Import session into app.py, [create a secret key for authentication](https://github.com/suitsuke/CS_BulletinBoard/blob/f49f0aebe0c7829bb26b2ef5c944a30b65e7f7de/app.py#L9), and replace the affected functions with the session-functionality, which now includes the csrf authentication and the secret key:

[Authenticating a logged in user or admin,](https://github.com/suitsuke/CS_BulletinBoard/blob/f49f0aebe0c7829bb26b2ef5c944a30b65e7f7de/app.py#L25-L34)

[logging in a user](https://github.com/suitsuke/CS_BulletinBoard/blob/f49f0aebe0c7829bb26b2ef5c944a30b65e7f7de/app.py#L142-L148)

[and logging out.](https://github.com/suitsuke/CS_BulletinBoard/blob/f49f0aebe0c7829bb26b2ef5c944a30b65e7f7de/app.py#L151-L154)