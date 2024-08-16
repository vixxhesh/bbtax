from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_home, name='admin_home'),
    path('appointments/', views.list_appointments, name='list_appointments'),
    path('contacts/', views.list_contacts, name='list_contacts'),
    path('appointments/delete/<int:pk>/', views.delete_appointment, name='delete_appointment'),
    path('contacts/delete/<int:pk>/', views.delete_contact, name='delete_contact'),
]
