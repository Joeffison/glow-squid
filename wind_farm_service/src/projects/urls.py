from django.urls import path

from projects import views

urlpatterns = [
    path('', views.get_projects, name='list_projects'),
]
