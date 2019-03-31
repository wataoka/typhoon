import json
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    f = open('data/data.json', 'r')
    data = json.load(f)
    years = list(map(lambda x: str(x), reversed(range(1999, 2020))))
    f.close()
    return render_template('/index.html', data=data, years=years)

if __name__ == "__main__":
    app.run(debug=True)
