from flask import Flask, jsonify, abort, render_template
import sqlite3

app = Flask(__name__)


def run_sql_query(qry):
    con = sqlite3.connect('./data/db.sqlite')
    data = [r for r in con.execute(qry).fetchall()]
    if len(data) == 0:
        abort(404)
    return data


@app.route('/', methods=['GET'])
def home():
    qry = "SELECT COUNT(*) FROM crunch;"
    count = run_sql_query(qry)[0][0]

    qry = "SELECT * FROM crunch;"
    records = run_sql_query(qry)
    return render_template('home.html', count=count, records=records)


@app.route('/random')
def show_random_record():
    qry = "SELECT COUNT(*) FROM crunch;"
    count = run_sql_query(qry)[0][0]

    qry = "SELECT * FROM crunch ORDER BY RANDOM() LIMIT 1;" 
    data = run_sql_query(qry)
    return render_template('article.html', count=count, record=data)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
