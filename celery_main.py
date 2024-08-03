from celery import Celery
import time

# for the return response from celery include backend="rpc://"

app = Celery("celery_main", backend="rpc://", broker="pyamqp://guest@localhost//")


@app.task
def task_queue(message):
    time.sleep(10)
    print(f"Celery QueueMessage: {message}")
    return "Task Queue message executed"
