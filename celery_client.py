from celery_main import task_queue

response = task_queue.delay("This is Shiv from celery client")
print(f"Response from celery app: {response.get()}")
