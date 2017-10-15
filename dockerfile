# Use an official Python runtime as a parent image
FROM python:2.7

ADD requirements.txt /app/requirements.txt

#set working dir to /app
WORKDIR /app

RUN apt-get update && apt-get install -yq less sudo octave && apt-get install -yq less python-pip && apt-get clean
RUN pip install -r requirements.txt

#copy current dir to /app
ADD . /app

WORKDIR /app/BENCHOP

# Run app.py when the container launches
CMD ["octave", "quicktable.m"]
