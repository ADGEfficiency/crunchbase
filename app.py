from flask import Flask, jsonify, abort
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/news/api/v1.0/source/<string:source>', methods=['GET'])
def count_source(source):
    sources = []
    qry = "SELECT COUNT(*) FROM berlin WHERE source_id = '%s';" % (source)
    con = sqlite3.connect('/home/soobrosa/berlin.sqlite')
    c = con.cursor()
    c.execute(qry)
    rows = c.fetchall()
    for row in rows:
        sources.append(row)
    c.close()
    if len(row) == 0:
        abort(404)
    return jsonify({'source_count': sources[0]})

if __name__ == '__main__':
    app.run(debug=True)
