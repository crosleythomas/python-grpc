FROM python:3.8-slim-buster

RUN mkdir -p /usr/src/app

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

CMD [ "python", "./sample_server.py" ]