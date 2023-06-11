# Minimal Airflow Docker

## How to run

```
docker-compose up -d
```

## Docker stats

Using LocalExecutor, PostgreSQL and Adminer:

```
CONTAINER ID   NAME                                CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
bdaf864c6315   minimal-airflow-docker-airflow-1    3.46%     723.6MiB / 3.837GiB   18.42%    6.54MB / 10.5MB   0B / 0B     78
a4fb2b9abb5a   minimal-airflow-docker-adminer-1    1.70%     17.47MiB / 3.837GiB   0.44%     99.5kB / 406kB    0B / 0B     1
ea79149d351a   minimal-airflow-docker-postgres-1   3.72%     69.19MiB / 3.837GiB   1.76%     8.28MB / 6.36MB   0B / 0B     20
```