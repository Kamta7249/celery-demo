from django.shortcuts import render
# from myceleryproject.celery import add
from myapp.tasks import *
from celery.result import AsyncResult
from myapp.tasks import generate_bulk_data
from django.http import JsonResponse


# Create your views here.

# # Enqueue Task using delay()
# def index(request):
#     # print("Result")
#     # res1 = add(10, 20)
#     res1 = add.delay(10, 20)
#     print("Result1:", res1)
#     # res2 = sub(100, 90)
#     # res2 = sub.delay(100, 90)
#     # print("Result2:", res2)
#     return render(request, "myapp/home.html")

# # Enqueue Task using apply_async
# def index(request):
#     print("Result")
#     # res1 = add(10, 20)
#     res1 = add.apply_async(args=[10, 20])
#     print("Result1:", res1)
#     # res2 = sub(100, 90)
#     res2 = sub.apply_async(args=[100, 90])
#     print("Result2:", res2)
#     return render(request, "myapp/home.html")

# Display addition value after task execution.
# def index(request):
#     result = add.delay(10,20)
#     result = generate_bulk_data.delay(10)
#     return render(request, "myapp/home.html", {'result':result})
#     # return render(request, "myapp/generate_bulk_data.html", {'result':result})

def index(request):
    # Call the Celery task to generate bulk data
    # bulk_data = generate_bulk_data(10)  # Generate 1000 records.
    bulk_data = generate_bulk_data.delay(10).get()  # Generate 1000 records.]
    # bulk_data = generate_bulk_data.apply_async(args=[10])
    
    # Pass the entire bulk_data.result list to the template
    return render(request, "myapp/generate_bulk_data.html", {'bulk_data': bulk_data})
    # return JsonResponse(bulk_data,safe=False)


# def check_result(request, task_id):
#     # Retrive the task result using the task_id
#     result = AsyncResult(task_id)
#     print("Ready: ", result.ready())
#     print("Successful: ", result.successful())
#     print("Failed: ", result.failed())
#     # print("Get: ", result.get())
#     return render(request, "myapp/result.html", {'result':result})


def check_result(request, task_id):
    # Retrieve the task result using the task_id
    result = AsyncResult(task_id)
    task_result = None

    # Check if the task is ready and successful
    if result.ready() and result.successful():
        # Get the task result if the task is successful
        task_result = result.get()

    return render(request, "myapp/task_result.html", {'bulk_data': task_result})


def about(request):
    print("Result")
    return render(request, "myapp/about.html")

def contact(request):
    print("Result")
    return render(request, "myapp/contact.html")