FROM ubuntu:latest
LABEL authors="TemaDrakoshef"

ENTRYPOINT ["top", "-b"]

FROM python:3.10.9

RUN mkdir /wisebot
WORKDIR /wisebot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn src.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000