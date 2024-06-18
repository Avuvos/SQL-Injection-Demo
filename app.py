from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


def initialize_database():
    print("Initializing database...")
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
    cursor.execute("INSERT INTO users VALUES ('admin', '1234')")
    connection.commit()
    connection.close()


@app.route('/')
def homepage():
    return render_template("login.html")


# fails to username = ' OR 1=1 -- and whatever password
@app.route('/vulnerable_login', methods=['POST'])
def insecure_login():
    username = request.form['username']
    password = request.form['password']
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    connection.close()
    if user is not None:
        return "Logged in!"
    else:
        return "Wrong username or password!"

# safe against sql injection
@app.route('/secured_login', methods=['POST'])
def secured_login():
    username = request.form['username']
    password = request.form['password']
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    query = f"SELECT * FROM users WHERE username =? AND password =?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    connection.close()
    if user is not None:
        return "Logged in!"
    else:
        return "Wrong username or password!"

if __name__ == '__main__':
    initialize_database()
    app.run()
