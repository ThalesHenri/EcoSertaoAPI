FROM python:3.11-alpine3.18

LABEL maintainer="Dennis"

ENV PYTHONDONTWRITEBYTECODE="1"
ENV PYTHONUNBUFFERED="1" 

COPY ./ecoApi /ecoApi
COPY ./scripts /scripts

WORKDIR /ecoApi

EXPOSE 8081

RUN python -m venv /venv && \
/venv/bin/pip install --upgrade pip && \
/venv/bin/pip install -r /ecoApi/requirements.txt && \
adduser --disabled-password --no-create-home duser && \
mkdir -p /data/ && \
chown -R duser:duser /data && \
chmod -R 755 /data && \
chmod -R +x /scripts

ENV PATH="/scripts:/venv/bin:$PATH"

USER duser

CMD ["commands.sh"]
#RUN pip install --upgrade pip
#RUN pip install --no-cache -r requirements.txt 

#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8081"]