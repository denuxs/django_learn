# django_learn

## Requirements
* Install Python 3
* Install Redis

## Packages
* django
* celery
* redis

## Develop

Run Server Celery

```bash
$ celery -A django_learn worker -l info
```

Run App

```bash
$ python manage.py runserver
```