Example of flask app:

```python
import sqlite3
import subprocess

from flask import Flask, render_template

app = Flask(__name__)

SQL_QUERY = \
"""
select ROUND(value) as v,
count(CASE WHEN entity = 'a' THEN 1 END) as a,
count(CASE WHEN entity = 'b' THEN 1 END) as b,
count(CASE WHEN entity = 'c' THEN 1 END) as c,
count(CASE WHEN entity = 'd' THEN 1 END) as d,
count(CASE WHEN entity = 'e' THEN 1 END) as e,
count(CASE WHEN entity = 'f' THEN 1 END) as f
from data
WHERE v > 0
group by v
;
"""

DB_PATH_PROD = '/shared/db/data.sqlite3'
DB_PATH_DEV = '/vagrant/data_test/docker-spark/shared/db/data.sqlite3'


# Function that stores query data as a dict instead of a tuple
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def get_graph():
    with sqlite3.connect(DB_PATH_PROD) as conn:
        conn.row_factory = dict_factory
        c = conn.cursor()
        c.execute(SQL_QUERY)
        data = {'chart_data': c.fetchall()}
    return render_template('index.html', data=data)


@app.route('/submit', methods=['GET'])
def submit():
    res = subprocess.call(
        '/spark/bin/spark-submit '
        '--master spark://spark-master:7077 '
        '--jars /shared/jars/sqlite-jdbc-3.23.1.jar '
        '--py-files /shared/dependencies/chardet.zip '
        '/shared/spark-apps/app.py', shell=True)
    return str(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```
