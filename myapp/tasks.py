from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json
from faker import Faker

@shared_task
def generate_bulk_data(num_records):
    """
    Generate bulk data using Faker library.
    
    Parameters:
    - num_records (int): Number of records to generate.
    
    Returns:
    - list: List of dictionaries containing fake data.
    """
    fake = Faker()
    bulk_data = [{'name': fake.name(), 'email': fake.email()} for _ in range(num_records)]
    return bulk_data

# @shared_task
# def sub(x, y):
#     sleep(10)
#     return x - y

# @shared_task
# def clear_session_cache(id):
#     print(f"Session Cache Cleared: {id}")
#     return id

# @shared_task
# def clear_redis_data(key):
#     print(f"Redis Data Cleared: {key}")
#     return key

# @shared_task
# def clear_rabbitmq_data(key):
#     print(f"RabbitMQ Data Cleard: {key}")
#     return key

# # Create Schedule every 30 seconds
# schedule, created = IntervalSchedule.objects.get_or_create(
#     every = 30,
#     period = IntervalSchedule.SECONDS,
# )

# # Schedule the periodic task programatically.
# PeriodicTask.objects.get_or_create(
#     name = 'Clear RabbitMQ Periodic Task',
#     task = 'myapp.tasks.clear_rabbitmq_data',
#     interval = schedule,
#     args = json.dumps(['Hello']), # Pass the arguments to the task as a JSON-encoded list
# )