from flask import Flask
from flask import render_template


def run(key):

    print(key)

    app = Flask(__name__)

    @app.route('/')
    def hello():

        s = "http://localhost:5000"
        print("somethign")
        return render_template("index.html",server=s)
    
    @app.route('/ack',methods=["POST"])
    def ack():
        print("Message has been acknowledged")
        return render_template("index.html",server="other server")


    app.run()