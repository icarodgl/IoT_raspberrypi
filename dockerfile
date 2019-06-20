FROM python:3.6-slim

COPY ./requirements.txt /tmp
COPY . /run
RUN pip install --no-cache-dir -r /tmp/requirements.txt

