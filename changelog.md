# 23.4.2024
projekti luotu
perustoiminnallisuudet lisätty
kirjautuminen ei toimi kokonaan
salasanan tarkastus toimii, mutta hyväksyy edelleen mitä vaan jolloin annetaan eväste että on kirjautunut sisään
ilmoittaa oikein väärät salasanat ja käyttikset
seuraavaksi katso kirjautuminen: app.py löytyy kohta TODO

admin pystyy poistamaan ja muokkaamaan
taviskäyttäjä pystyy postaamaan
ehkä lisätoiminnallisuus, ei tarvitse tähän tehtävään? pitäisikö viestissä näkyä username kuka postasi?
tunteja: 6

# 24.4.2024
kirjautuminen toimii, sekä sisään että ulos
admin voi muokata ja poistaa, tavallinen käyttäjä voi kirjoittaa

seuraavaksi tehdään tietoturvaongelmat
tunteja: 2

# 25.4.2024
xss-ongelma lisätty
aloitetaan injektiota
tunteja:

# Steps to fix
5. csrf token sent with cookies
käytä sessionia korjataksesi
muista tehdä turvallinen avain joka autentikoi
- editoi app.py tiedostoa

4. xss - ongelma (käyttäjä voi antaa koodia ikkunoihin)
käytä jinjan sisäänrakennettuja toimintoja jotka automaattisesti sanitizes input stuff, älä palauta sivua suoraan html, luo index.html ja käytä jinjan toimintoja
nyt voi kirjoittaa vaikka script>alert("You have been hacked!") /script> tai muotoilua kenttiin h1> text /h1>
- lisätään index.html jossa jinja tekee asiat kauniisti ja turvallisesti
- lisäksi poistetaan app.py tiedostosta index-funktion palautus ja renderöidään vaan index.html

3. sql-injektio-ongelma


2. hashed passwords

1. user: admin, pw: admin