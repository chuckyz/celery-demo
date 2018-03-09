# celery-demo
Demo repo for Celery

```
docker-compose up -d

python3 -m venv venv

source venv/bin/activate

celery -A demo_tasks worker --loglevel=INFO

python demo.py

php demo.php
```
