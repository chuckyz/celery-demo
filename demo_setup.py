import subprocess as sub
import shlex

sub.call(shlex.split('mysql -h 127.0.0.1 -ucelery -pcelery celery -e "drop table celery"'))
sub.call(shlex.split('mysql -h 127.0.0.1 -ucelery -pcelery celery -e "create table celery (id int(11) unsigned NOT NULL AUTO_INCREMENT, created_at timestamp NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (`id`))"'))
for _ in range(100):
    sub.call(shlex.split('mysql -h 127.0.0.1 -ucelery -pcelery celery -e "INSERT INTO celery (id) VALUES (0),(0),(0),(0),(0),(0),(0),(0),(0),(0),(0);"'))
