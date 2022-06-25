# celery-basics
A Django project demonstrating execution of tasks through Celery

## Dependencies
- Django
- RabbitMQ
- Erlang (for RabbitMQ)
- Celery
- gevent (for Windows)

> pip install django celery gevent
* Setup RabbitMQ server manually

## Running the celery app for listening
![image](https://user-images.githubusercontent.com/50711734/175760344-9d9d2a67-917a-4ede-a64f-bf22c5f18520.png)

## Putting in commands from project's Python shell
- add.delay(4,4)
- add.apply_async((4,4), countdown=10)
![image](https://user-images.githubusercontent.com/50711734/175760637-c4fb9bfa-1e8b-43aa-91f0-592a3993fae3.png)

## Results on Celery prompt
- add.delay(4,4) computed and returned immediately => in red
- add.apply_async((4,4), countdown=10) waited for 10 seconds before computing and returning the result => in blue; Notice the difference between time at which the request is 'received' and 'succeeded'.
![image](https://user-images.githubusercontent.com/50711734/175760644-3e381730-d916-4107-a7ce-d6e9ac63c4c3.png)
