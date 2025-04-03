from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jobs/", views.index, name="index2"),
    path("jobs/<str:location>/", views.jobsinlocation, name="jobs_in_location"),
    path("ht/health-check", views.MyHealthCheck)
]