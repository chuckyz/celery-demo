from celery import Celery
import time, random

app = Celery('celery')
app.config_from_object('celeryconfig')

@app.task
def add(x,y):
    return x+y

@app.task
def slow_add(x,y):
    time.sleep(random.randint(5,20))
    return x+y

@app.task
def multiply(x,y):
    return x*y

