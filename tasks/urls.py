from django.urls import path
from . import views
from rest_framework import  routers

router=routers.DefaultRouter()

# router.register('task',views.TaskViewSet,basename='tasks')
router.register('task',views.TaskModelViewSet,basename='task')


urlpatterns = [
    path('projects/',views.ProjectApiView.as_view(),name='projects_list'),
    path('projects/<int:pk>/',views.ProjectApiView.as_view(),name='project_detail'),
    path('projects/<int:pk>/task/list/',views.ProjectDetailTaskAPIView.as_view(),name='project_detail_tasks'),
    # path('tasks/',views.TaskApiView.as_view(),name='task_list'),
    # path('tasks/<int:pk>/',views.TaskDetailApiView.as_view(),name='task_detail')




    ]+router.urls


