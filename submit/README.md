# Spark submit

The Spark submit image serves as a base image to submit your application on a Spark cluster. This may be either a Java, Scala or Python application. See [big-data-europe/docker-spark README](https://github.com/big-data-europe/docker-spark) for a description how to submit your own application to a Spark cluster.

By default the image opens 5000 port for flask applications, which is located
in "api" directory.
