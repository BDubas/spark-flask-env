FROM bdubas/spark-base:latest

ENV SPARK_MASTER_NAME spark-master
ENV SPARK_MASTER_PORT 7077

COPY api /api

WORKDIR /api
RUN pip3 install -r requirements.txt

CMD ["python", "app.py"]