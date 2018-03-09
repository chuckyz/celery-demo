# celery-demo
Demo repo for Celery

```
docker-compose up -d

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

composer install

celery -A demo_tasks worker --loglevel=INFO

python demo.py

php demo.php
```
