# app.py
includes the routes

# | safe 
 Warning: Using the safe filter on HTML from unknown data sources may open up your application to XSS attacks. Do not use it unless the HTML you are rendering is from a trusted source.

# escape
the escape() function renders the word string as text. 
This is important to avoid Cross Site Scripting (XSS) attacks. 
If the user submits malicious JavaScript instead of a word, 
escape() will it render as text and the browser will not run it, keeping your web application safe.

## Tietoturvaongelmat

# A1:2017-Injection: sql-injektio
tietokantajuttuja

# A7:2017-Cross-Site Scripting (XSS) xss-haavoittuvuus
data joka tallennetaan on sellainen jonka pitää näkyä muille / haitata muiden käyttäjien katselemia sivuja jotta se on ongelma

# csrf-haavoittuvuus
ei varmenneta että postaus/request tulee oikeasti oikealta tyypiltä
secret key flaskissa

# A9:2017-Using Components with Known Vulnerabilities
laittaa vanhan version jostain riippuvuudesta
flask on vanha?

# A6:2017-Security Misconfiguration
admin-käyttäjä: admin admin

# A3:2017-Sensitive Data Exposure
salasanat tallennetaan plaintextinä tietokantaan


## appin toiminta
simppeli web-app johon kirjaudutaan
kun on kirjautunut, pystyy tekemään postaamaan viestejä sivulle näkyviin kaikille
admin pystyy poistamaan kaikkien viestejä
viestit on tietokannassa sqlite3 ja ne haetaan sieltä ja renderöidään

# readme
pip install flask
pip install flask-wtf
export FLASK_APP=app
export FLASK_ENV=development
flask --debug run

# rakennusohjeet
ensiksi display sisältö 
sen jälkeen rakennetaan post-toiminto