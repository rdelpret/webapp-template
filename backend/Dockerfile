FROM python:3.7

WORKDIR /app

ADD . . 

RUN pip3 install -r requirements.txt 

ENV PYTHONPATH $PYTHONPATH:/app/backend

EXPOSE 8000
