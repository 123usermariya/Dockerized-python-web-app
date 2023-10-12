from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:admin123@database-1.cccicy4zloz7.ap-south-1.rds.amazonaws.com:3306/db1'
db = SQLAlchemy(app)

# Define a simple database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    with app.app_context():
    # Create the database tables (you should do this once)
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=80)
