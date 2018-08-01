# edss

## Docker Setup (`docker` branch)
1. Install `docker` and `docker-compose`.
2. run `make run` in the root directory (this one)

## Activate Environment (be in top root folder)
```
# install python 3.6.+ and virtualenv if you haven't already
virtualenv --no-site-packages dev_env
source dev_env/bin/activate
pip install -r requirements.txt
```

## Run backend
```
$ cd student_showcase
$ python manage.py runserver
```
