# python-flask

Skeleton code for a simple Python/Flask application with the following setup:

* Rest API
* Server side session management
* API key authentication

## Docker

### Cleanup

``docker container ls -a`` -> ``docker container rm -f [name or id]``

``docker image ls`` -> ``docker image rm -f [repository or id]``

### Build image/container

``docker build -t python-flask .``

``docker run --name python-flask --env-file .env -p 5002:5002 python-flask``

### Deploy to Google Cloud

 ``gcloud config set project <PROJECT_ID>`` -> ``gcloud projects list`` and ``gcloud config get-value project``

``gcloud builds submit --tag gcr.io/<PROJECT_ID>/python-flask``
