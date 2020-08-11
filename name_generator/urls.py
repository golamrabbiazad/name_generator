
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("generator_app.app_urls")),
    path('generate/', include("generator_app.app_urls")),
    path('tasks/', include("tasks.app_urls")),
    path('newyear/', include("newyear.app_urls"))
]
