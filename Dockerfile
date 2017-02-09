FROM mdillon/postgis
COPY ./database_config.sh /docker-entrypoint-initdb.d/database_config.sh

FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
