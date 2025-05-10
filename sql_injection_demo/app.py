from flask import Flask, render_template, request, redirect, url_for, flash, session
import clientsocket
import db_connector
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For session management

# Get database connection
# Provide your database connection details here
host = "127.0.0.1"
port = 3306
user = "root"
password = "kali"
con_obj = db_connector.Connector(host, port, user, password)
api_key = ''

if con_obj.cnx.is_connected():
    print('...Connected to MySQL server...')
else:
    print("...Error connecting to mysql server...")

def getapikey(uname,passwd):
    global api_key
    query = "select api_key from employee where uname='{uname}' and passwd='{passwd}'"
    checker_obj = json.dumps({"og_query":query,"input_vals":{"uname":uname,"passwd":passwd}})
    res = clientsocket.checkquery(checker_obj)
    if res == '1':
        print(query.format(uname=uname,passwd=passwd))
        con_obj.execute_query(query.format(uname=uname,passwd=passwd))
        api_key = con_obj.cur.fetchone()
        print(api_key)
        if api_key:
            api_key = api_key[0]
            return api_key
        else:
            return None
    else:
        return 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(request.form)
        api_key = getapikey(username,password)
        
        if api_key == 0:
            # SQL injection detected, block login and log incident
            flash("Potential SQL injection detected. Login blocked.")
            return redirect(url_for('index'))
        if api_key == None:
            flash("Invalid Username Or Password")
            return redirect(url_for('index'))

        # Validate user credentials (log in for any safe input)
        session['user'] = username
        return redirect(url_for('dashboard'))
    
    return render_template('index.html')

# Dashboard route, only accessible after successful login
@app.route('/dashboard')
def dashboard():
    global api_key
    if 'user' not in session:
        return redirect(url_for('index'))
    
    return render_template('dashboard.html', username=session['user'], key=api_key)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
