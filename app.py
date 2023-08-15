from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Speedster',
        'location': 'Tokyo, Japan',
        'salary': '¥ 90,00,000'
    },
    {
        'id': 2,
        'title': 'Space Scientist',
        'location': 'Metropolis, USA',
        'salary': '$ 100,000'
    },
    {
        'id': 3,
        'title': 'Damage Analyst',
        'location': 'Gothan, USA',
        'salary': '$ 80,000'
    },
    {
        'id': 4,
        'title': 'Super Human',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 35,00,000'
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs = JOBS, company_name = 'Justice League')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)