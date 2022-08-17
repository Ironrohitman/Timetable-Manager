from flask import Flask, request, render_template,jsonify
import webbrowser
from threading import Timer
import pywhatkit
import json


from flask import request


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


def open_browser():
    webbrowser.open_new('http://127.0.0.1:2000/')

@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    print(output)  # This is the output that was stored in the JSON within the browser

    return {}



#rendering the HTML page which has the button
@app.route('/json')
def json():
    return render_template('index.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    pywhatkit.sendwhats_image("+61402456069 ", "rotato.png", "Hello i have sent this from the bunny himself")
    print("Hello")
    return("nothing")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(port=2000)

