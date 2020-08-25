FROM python:3.6-slim AS server

RUN mkdir /server
WORKDIR /server

RUN pwd
RUN ls -la
COPY ./server/requirements.txt /server/
RUN pip install -r requirements.txt

COPY ./server /server
RUN python ./manage.py collectstatic --noinput
