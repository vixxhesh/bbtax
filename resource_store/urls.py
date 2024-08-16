from django.urls import path
from .views import upload_resource, resource_list

urlpatterns = [
    path('upload/', upload_resource, name='upload_resource'),
    path('', resource_list, name='resource_list'),
]
