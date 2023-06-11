FROM apache/airflow:slim-2.6.1-python3.10

RUN pip install psycopg2-binary

COPY entrypoint.sh entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]