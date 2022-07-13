FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /sentimental-analysis

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

