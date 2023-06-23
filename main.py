from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'data analyst',
    'location': 'bengaluru,india',
    'sallary': 'rs 1000000'
  },
  {
    'id': 1,
    'title': 'data analyst',
    'location': 'bengaluru,india',
    'sallary': 'rs 1000000'
  },
  {
    'id': 1,
    'title': 'data analyst',
    'location': 'bengaluru,india',
    'sallary': 'rs 1000000'
  },
  {
    'id': 1,
    'title': 'data analyst',
    'location': 'bengaluru,india',
    'sallary': 'rs 1000000'
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ =="__main__":
  app.run(host='0.0.0.0', debug=True)