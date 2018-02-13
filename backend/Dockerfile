FROM python:3.6
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    mysql-client \
    libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi
COPY . .

# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
