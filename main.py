from flask import Flask, render_template, request, jsonify
import sqlite3
import waf  # Import the WAF file

app = Flask(__name__)

# Database connection and table creation
conn = sqlite3.connect('mertttttt.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
conn.commit()

# Create a list to store incoming requests
requests_list = []

# Integrate and start the WAF file with the Flask application
waf.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Retrieve user login and create an SQL query
    sql = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    c.execute(sql)
    result = c.fetchone()

    # Add the incoming request to the requests_list list
    requests_list.append({'username': username, 'password': password})

    if result:
        return 'Login successful!'
    else:
        return 'Incorrect username or password!'

@app.route('/requests')
def show_requests():
    # Return the requests_list list in JSON format
    return jsonify(requests_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)
