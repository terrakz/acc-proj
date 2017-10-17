# Use an official Python runtime as a parent image
FROM completeoctave

#copy current dir to /app
ADD . /app

WORKDIR /app
ENTRYPOINT celery -A celery_part worker --app=celery_part.celery_app --concurrency=20 --loglevel=info
