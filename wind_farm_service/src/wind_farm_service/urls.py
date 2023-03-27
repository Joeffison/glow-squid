from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    re_path(r'^api/v1/projects/', include('projects.urls')),
    path('admin/', admin.site.urls),
]
