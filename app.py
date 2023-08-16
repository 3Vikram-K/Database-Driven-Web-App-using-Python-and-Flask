from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Tokyo, Japan',
        'salary': '¥ 140,00,000'
    },
    {
        'id': 2,
        'title': 'Web Developer',
        'location': 'New York, USA',
        'salary': '$ 100,000'
    },
    {
        'id': 3,
        'title': 'DevOps Engineer',
        'location': 'Bengaluru, India',
        'salary': '$ 30,00,000'
    },
    {
        'id': 4,
        'title': 'Senior Software Engineer',
        'location': 'Hyderbad, India',
        'salary': 'Rs. 55,00,000'
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs = JOBS, company_name = 'VYKRAM')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)