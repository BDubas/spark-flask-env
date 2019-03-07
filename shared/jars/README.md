Shared directory for storing jars required for running a spark job.

Example of usage in flask endpoint:

```python
@app.route('/submit', methods=['GET'])
def submit():
    res = subprocess.call(
        '/spark/bin/spark-submit '
        '--master spark://spark-master:7077 '
        
        '--jars /shared/jars/sqlite-jdbc-3.23.1.jar '
        
        '/shared/spark-apps/app.py', shell=True)
    return str(res)
```