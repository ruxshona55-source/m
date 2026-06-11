from django.urls import path
from . import views

urlpatterns = [
    path('projects/',views.ProjectApiView.as_view(),name='tasks'),
    path('projects/<int:pk>/',views.ProjectApiView.as_view(),name='tasks'),


]