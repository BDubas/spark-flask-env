PySpark applications that should be submitted from an endpoint in 
"shared" container.

Example:

```python
"""Pyspark application."""

from pyspark.sql import SparkSession
import chardet


def extract_records(file_record):
    """Extract records from a string with '\n' delimiter.

    Args:
        file_record (tuple) - file_name (str), content (str)
    Return:
        list of lists [[str, float, str]...]
    """
    data = file_record[1]
    encoding_line, *data_lines = data.split(b'\n', 6)
    encoding = encoding_line.decode().split('=')[1]
    for i, line in enumerate(data_lines):
        data_lines[i] = line.decode(encoding).split(',', 2)
        # Check if at least the first two chars were decoded correctly
        if data_lines[i][0] not in ['a', 'b', 'c', 'd', 'e', 'f']:
            # If any exception is raised during the second decoding,
            # the whole file is skipped
            try:
                data_lines[i] = \
                    line.decode(chardet.detect(line)['encoding']).split(',', 2)
            except:
                return []
        try:
            float(data_lines[i][1])
        except ValueError:
            return []

    return data_lines


def job():
    """Pyspark job.

    1. Create RDD with (str, float, str) records.
    2. Convert RDD into DataFrame and perform db insert.
    """
    spark = SparkSession.builder.appName('Parser').getOrCreate()

    rdd = spark.sparkContext \
        .wholeTextFiles('file:///shared/data/test-*', use_unicode=False) \
        .flatMap(extract_records)

    spark.createDataFrame(rdd, ['entity', 'value', 'string']) \
        .write \
        .mode('append') \
        .format('jdbc') \
        .options(url='jdbc:sqlite:/shared/db/data.sqlite3',
                 dbtable='data',
                 numPartitions='1',
                 driver="org.sqlite.JDBC") \
        .save()


if __name__ == '__main__':
    job()
```