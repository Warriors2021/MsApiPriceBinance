# Definir la imagen base de Docker
FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt /app
COPY main.py /app
COPY ConexionMongo.py /app
COPY ConexionAPICriptowath.py /app

RUN pip install --no-cache-dir -r requirements.txt

ENV HOST_MONGO=localhost
ENV DB_MONGO=DbTest
ENV MONEDAS=btcusdt,ethusdt
ENV APIKEY=key


EXPOSE 8000

CMD ["python","main.py"]
