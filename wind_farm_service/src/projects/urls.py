from django.urls import path

from projects import views

urlpatterns = [
    path('', views.project_list, name='list_projects'),
    path('<int:pk>', views.project_detail, name='projects_detail'),
]
