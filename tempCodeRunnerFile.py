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
                 return redirect('/')
            else:
                return "Invalid email or password. Please try again."

    return render_template('login.html')
