import os
import sqlite3
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

    create_files_table_sql = """
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY,
        filename TEXT NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id)
    );
    """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        c.execute(create_files_table_sql)
    except sqlite3.Error as e:
        print(e)

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

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
            user_id = cursor.lastrowid
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
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (email, password))
            user = cursor.fetchone()
            if user:
                return redirect('/')
            else:
                return "Invalid email or password. Please try again."

    return render_template('login.html')

# Route for file upload
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        user_id = request.form['user_id']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        conn = create_connection('database.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO files (filename, user_id) VALUES (?, ?)", (filename, user_id))
            conn.commit()
            return "File uploaded successfully."
    return render_template('upload.html')

@app.route('/view_files', methods=['GET'])

def view_files():
    conn = create_connection('database.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, filename, user_id FROM files")
        files = cursor.fetchall()
        return render_template('view_files.html', files=files)

if __name__ == '__main__':
    conn = create_connection('database.db')
    create_table(conn)
    app.run(debug=True)
