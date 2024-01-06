FROM python:3.10-alpine

COPY requirements.txt /temp/requirements.txt
COPY CountrySeek /CountrySeek

WORKDIR CountrySeek

EXPOSE 8000

RUN apk add --no-cache postgresql-client build-base postgresql-dev && \
    pip install --no-cache-dir -r /temp/requirements.txt

RUN adduser --disabled-password country-user

USER country-user