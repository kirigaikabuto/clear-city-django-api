# pull official base image
FROM python:3.9
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt
RUN python manage.py makemigrations
# copy project
COPY . .

EXPOSE 5002