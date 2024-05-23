ARG PYTHON_VERSION=3.12.0
FROM python:${PYTHON_VERSION}-slim as base

RUN apt-get update

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 8000
