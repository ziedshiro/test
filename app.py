import os
from flask import Flask,render_template
import pyrebase

firebaseConfig={'apiKey': "AIzaSyAkMTo42DRB-G8LSfJ3AgCXwb_iedD9Z9k",
  'authDomain': "knotice-6acbd.firebaseapp.com",
  'databaseURL': "https://knotice-6acbd-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "knotice-6acbd",
  'storageBucket': "knotice-6acbd.appspot.com",
  'messagingSenderId': "64940370131",
  'appId': "1:64940370131:web:758cfa20615773d4890c26"}

firebase=pyrebase.initialize_app(firebaseConfig)
storage=firebase.storage()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('web.html',test1="123",test2=storage.child("1.png").get_url(None))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
