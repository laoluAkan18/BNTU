from flask import Flask, request, render_template, redirect

import os


def run(key):

    print(key)

    app = Flask(__name__)

    @app.route('/')
    def hello():
        key = os.environ.get("apod-key")
        apod_url = f"https://api.nasa.gov/planetary/apod?api_key={key}"

        s = "http://localhost:5000"
        print("somethign")
        return render_template("index.html",server=s,key=key)
    
    @app.route('/',methods=["POST"])
    def ack():
        print("Message has been acknowledged")
        return render_template("index.html",server="other server")
    
    @app.route('/populate-key',methods=["POST"])
    def populate_key():
        print("populate key fetched")
        if 'key-input' in request.form:
            os.environ["apod-key"] = str(request.form['key-input'])
            return redirect("/",code=302)
        else:
            return render_template("404.html")


    app.run(debug=True)