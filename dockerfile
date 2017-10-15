# Use an official Python runtime as a parent image
FROM python:2.7
FROM debian:jessie

ADD requirements.txt /app/requirements.txt

# Set the working directory to /app
WORKDIR /app/

RUN apt-get update && apt-get install -yq less sudo octave && apt-get install -yq less python-pip && apt-get clean
RUN pip install -r requirements.txt

# Run app.py when the container launches
#CMD ["octave", "Table.m"]