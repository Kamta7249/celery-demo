from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('check-result/', views.check_result, name='check_result'),
    # path('result/<str:task_id>', views.check_result, name='check_result'),
    path('check-result/<str:task_id>/', views.check_result, name='check_result'),

]
