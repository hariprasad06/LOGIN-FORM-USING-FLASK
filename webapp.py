from flask import Flask, request, render_template
from flaskext.mysql import MySQL

sql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'  # configuration of  MySql database
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
sql.init_app(app)


@app.route('/')
def my_form():
    return render_template("form.html")  # calling html file using render_template


@app.route('/', methods=['POST'])
def access():
    username = request.form['username'] # request.form used to submit the Form
    password = request.form['password']
    db = sql.connect().db() # connecting to database
    db.execute("SELECT *FROM user where username='" + username + "' and password='" + password + "'")
    data = db.fetchone() # Select the values and fetch it from the Database
    if data is None:
        return "Your username and password is in correct"
    else:
        return "logged in successfully"


if __name__ == "__main__":
    app.run()
