#! /usr/bin/python3

#DOC#@CLI@$deprecated$ "Old script that sent me emails every morning"

import smtplib
import ssl
from email.message import EmailMessage
import random
import subprocess

albums = subprocess.run(['beet', 'ls', '-af', '$albumartist - $album ($original_year) [$genre] // $path', 'status:0'], capture_output=True)
albums = albums.stdout.decode('UTF-8').splitlines()
number_of_unheard = len(albums)
selected_album = random.choice(albums)
number_of_albums = len(subprocess.run('beet ls -a'.split(), capture_output =True).stdout.decode('UTF-8').splitlines())

name = selected_album.split(' // ')[0]
path = selected_album.split(' // ')[1]

email_sender = 'matiasylinenceau@gmail.com'
email_password = 'kazy iaxv cskk yseg'
email_receiver = 'matias@ceau.net'

subject = f"[A] {name}"
body = f"[A] {path} \n {number_of_unheard} unheard albums ({100 * round(number_of_unheard/number_of_albums,2)}%)"

em = EmailMessage()
em['From'] = 'Album du jour'
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
