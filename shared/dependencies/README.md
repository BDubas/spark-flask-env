This directory should contain python dependencies that are going to be
submitted to Spark cluster with "spark-submit" script via --py-files argument. 

For example, you can write flask module endpoint inside "submit"
container, which will submit spark a job that depends on
3rd-party python libraries:

app.py

```python
@app.route('/submit', methods=['GET'])
def submit():
    subprocess.call(
        '/spark/bin/spark-submit '
        '--master spark://spark-master:7077 '
        '--py-files /shared/dependencies/chardet.zip '
        '/shared/spark-apps/app.py', shell=True)
```