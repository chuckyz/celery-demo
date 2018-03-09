from demo_tasks import add,multiply,slow_add

jobs = [
    add.delay(2,2),
    add.delay(2,'a'),
    multiply.delay(2,2),
    slow_add.delay(2,2)
]

for job in jobs:
    try:
        print(job.status)
        print(job.get())
    except Exception as e:
        print(e)
        pass

slow_jobs=[]
for i in range(10):
    slow_jobs.append(slow_add.delay(i,i))

for job in slow_jobs:
    print(job.status)
    print(job.get())