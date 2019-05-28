FROM python:3.6

RUN pip3 install pip --upgrade \
    && pip3 install pipenv \
    && apt update \
    && apt install -y mysql-server \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /htdocs/www
WORKDIR /htdocs/www

EXPOSE 8000

ADD Pipfile /htdocs/www
ADD Pipfile.lock /htdocs/www
RUN pipenv install --dev
