FROM brianhgrant/hacko-geodjango
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN python
ADD . /code/
ENTRYPOINT [ "/code/bin/docker-entrypoint.sh" ]
