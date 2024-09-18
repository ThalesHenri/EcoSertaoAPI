FROM python:3.10-slim 

LABEL maintainer="Dennis"

EXPOSE 8081

RUN mkdir -p /opt/eco-sertao-api 
WORKDIR /opt/eco-sertao-api

COPY API .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache -r requirements.txt 

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8081"]
