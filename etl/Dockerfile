FROM python:3.10-slim-buster

WORKDIR apps

COPY apps/ .
COPY etl/ .
COPY requirements.txt .

pip install -r requirements.txt