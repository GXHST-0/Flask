from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sensor_data.db'
db = SQLAlchemy(app)
class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    motion = db.Column(db.Boolean)
    sound = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    data = SensorData.query.order_by(SensorData.timestamp.desc()).limit(100).all()
    return render_template('index.html', data=data)