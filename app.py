import json
from flask import Flask, render_template, url_for

from deviation import get_deviation

app = Flask(__name__)

@app.route('/')
def index():
    f = open('data/data.json', 'r')
    data = json.load(f)
    f.close()
    return render_template('/index.html', data=data)

@app.route('/deviation/<id>')
def deviation(id):
    f = open('data/data.json', 'r')
    data = json.load(f)
    f.close()

    typhoon = [x for x in data if x['id'] == int(id)][0]

    dev = get_deviation(int(typhoon['pressure']))

    return render_template('/deviation.html', typhoon=typhoon, dev=dev)

if __name__ == "__main__":
    app.run(address='0.0.0.0', debug=False)
