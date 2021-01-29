#!/usr/bin/env python3
import cgi, cgitb, os

cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
from secret import username, password
from http.cookies import SimpleCookie

new_stat = cgi.FieldStorage()

new_user = new_stat.getfirst("username")
new_pass = new_stat.getfirst("password")

correct = SimpleCookie(os.environ["HTTP_COOKIE"])

correct_user = None
correct_pass = None

cookie_ok = correct_user == username and correct_pass == password
stat_ok = new_user == username and new_pass == password

if correct.get("username"):
    correct_user = correct.get("username").value
if correct.get("password"):
    correct_pass = correct.get("password").value


if cookie_ok:
    new_user = correct_user
    new_pass = correct_pass

print("Content-Type: text/html")

if stat_ok:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

print()

if not new_user and not new_pass:
    print(login_page())
elif new_user == secret.username and new_pass == secret.password:
    print(secret_page(new_user, new_pass))
else:
    print(after_login_incorrect())



