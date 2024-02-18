import sqlite3
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Function to create a connection to the SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn

# Create a new SQLite database if not exists
def create_table(conn):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
    """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

# Route for signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        conn = create_connection('database.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (email, password))
            conn.commit()
            return redirect(url_for('login'))
    return render_template('signup.html')

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = create_connection('database.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (email , password))
            user = cursor.fetchone()
            if user:
                return "Login successful!"
            else:
                return "Invalid email or password. Please try again."

    return render_template('login.html')

if __name__ == '__main__':
    conn = create_connection('database.db')
    create_table(conn)
    app.run(debug=True)
