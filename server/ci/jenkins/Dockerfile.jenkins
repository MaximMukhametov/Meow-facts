FROM python:3.7-slim AS server
RUN pwd
RUN ls -la
RUN mkdir /server
RUN pwd
RUN ls -la
WORKDIR /server
RUN pwd
RUN ls -la
COPY requirements.txt /server/
RUN pip install -r requirements.txt
RUN pwd
RUN ls -la
COPY ./server /server
RUN python ./manage.py collectstatic --noinput