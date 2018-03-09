<?php
# Note: This is broken..  This class mirrors the broker and result backends, 
#   and as we are using rabbitmq/redis in this example it won't work.  
#   If rabbitmq+rpc (through AMQP) were used it would work.
require __DIR__ . '/vendor/autoload.php';

$c = new \Celery\Celery('localhost', 'guest', 'guest', '/');
$result = $c->PostTask('demo_tasks.add', array(2,2));

while (!$result->isReady())    {
    sleep(1);
    echo '...';
}

if ($result->isSuccess()) {
    echo $result->getResult();
} else {
    echo "ERROR";
    echo $result->getTraceback();
}
