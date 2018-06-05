FROM python:3.6.5-stretch
MAINTAINER Brian H. Grant <brian@hackoregon.org> & "M. Edward (Ed) Borasky <znmeb@znmeb.net>
ENV PYTHONUNBUFFERED 1

# add required Debian packages
# https://docs.djangoproject.com/en/2.0/ref/contrib/gis/install/geolibs/
RUN apt-get update \
  && apt-get install -qqy --no-install-recommends \
    binutils \
    gdal-bin \
    libproj-dev \
  && apt-get clean

# create and populate /code
RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN python
COPY . /code/

ENTRYPOINT [ "/code/bin/docker-entrypoint.sh" ]
