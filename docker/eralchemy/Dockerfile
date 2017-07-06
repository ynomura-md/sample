FROM python:2.7.13

ENV LANG=C.UTF-8

RUN apt-get update
RUN apt-get install graphviz libpq-dev -y

RUN pip install psycopg2==2.7.1
RUN pip install ERAlchemy==0.0.31
