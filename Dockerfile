FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR  /usr/app
COPY ./migrations migrations
COPY ./src src
COPY ./main.py main.py

EXPOSE 8000

