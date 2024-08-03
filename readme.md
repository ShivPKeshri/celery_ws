### Install celery
```
pip install celery
```

### Run celery
```
celery -A celery_main worker -l INFO
```

with the concurrency 2 workers (instances): 
```
celery -A celery_main worker -l INFO -c 2
or
celery -A celery_main worker -l INFO --concurrency=2
```