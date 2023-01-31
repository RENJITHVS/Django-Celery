# Django-Celery Machine Test

### Introduction

Here we Integrate the [Celery](https://docs.celeryq.dev/en/stable/) (a task queue) with Django application. Here we use the [Redis]('https://github.com/tporadowski/redis/releases') as Messagebroker, along with celery-results to store the task data to Database. so that a task to generate random csv file is performed by the Celery outside the django request-response cycle.

### Prerequisites

Your local machine must have following packages installed: 
```
    * Python
    * Redis
```

### Installation

* clone the repository:
* Create and setup virtual environment
* run the following command in root-folder
```
pip install -r requirements.txt
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
* This project is fully based on celery and django. So, the necessary modules installed are:
```
    * django==4.1.5
    * redis==4.4.2
    * django-celery-results==2.4.0
```
* activate the celery worker by running command, since the celery default prefork process have compactibility issue with windows.
```
celery -A django_celery.celery worker --pool=solo -l info

```
* else we can run the default run command 
```
celery -A django_celery worker -l info

```

### Testing

*  Trigger the Celery Task by providing the name of random-csv file and row count on the addressbar

```
 http://127.0.0.1:8000/<filename>/<row_count>

 eg: http://127.0.0.1:8000/firstdata/60

```
* log into the django admin to see the celery-task-result log.

