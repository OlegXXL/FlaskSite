from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///shop.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullabel=False)
    price = db.Column(db.Integer, nullabel=False)
    isActive = db.Column(db.Boolean, default=True)
    #text = db.Column(db.Text, default=True)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/user')
def user():
    return render_template('user.html')


if __name__ == '__main__':
    app.run()
