FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY data/recipes.csv data/recipes.csv

COPY app .

EXPOSE 8000

CMD gunicorn --bind 0.0.0.0:8000 app:app