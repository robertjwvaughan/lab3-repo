

from flask import Flask
from flask_mysqldb import MySQL
from flask import request
from flask import render_template
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ILoveGoogle'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.195.18.23'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format

@app.route("/add", methods=['GET'])
def add():
    # sid = request.args.get('id', '')
    name = request.args.get('name', '')
    email = request.args.get('email', '')
    
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute("INSERT INTO students (studentName, email) values ('"+name+"', '"+email+"')")
    conn.commit
    return str('Success')

@app.route("/update", methods=['GET'])
def update():
    name = request.args.get('name', '')

    cur = mysql.connection.cursor()
    cur.execute("UPDATE students SET studentName = 'Bob' WHERE studentName = '"+name+"'");

    cur.execute('''SELECT * FROM students''')
    rv = cur.fetchall()
    return str(rv)


@app.route("/delete", methods=['GET'])
def delete():
    name = request.args.get('name', '')

    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE studentName='"+name+"'")

    cur.execute('''SELECT * FROM students''')
    rv = cur.fetchall()
    return str(rv)

@app.route('/index/')
def index():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000
