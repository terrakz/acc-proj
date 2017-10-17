# Use an official Python runtime as a parent image
FROM octave3
RUN pip3 install --upgrade pip
RUN pip3 install scipy
RUN pip3 install numpy
RUN pip3 install oct2py

#copy current dir to /app
ADD . /app

WORKDIR /app
ENTRYPOINT celery -A celery_part worker --app=celery_part.celery_app --loglevel=info
