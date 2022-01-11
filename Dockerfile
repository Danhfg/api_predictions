# syntax=docker/dockerfile:1

FROM python:3.7

ADD . /python-flask
WORKDIR /python-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

COPY app.py app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]