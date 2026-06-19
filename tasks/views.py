from asyncio import tasks


from accounts import serializers
# from db.models import Model
from rest_framework import status
from  rest_framework.decorators import action
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.views import APIView
from tasks.models import Project, Task
from tasks.serializers import ProjectSerializer, TaskListSerializer, TaskCreateAndUpdateSerializer
from tasks.serializers import ProjectCreateAndUpdateSerializer
from rest_framework.response import Response



class ProjectApiView(APIView):
    def get(self, request):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)
        # project_list = []
        # for project in project:
        #     projects_dict = {
        #         'id': project.id,
        #         'name': project.name,
        #         'description': project.description,
        #     }
        #     project_list.append(projects_dict)
        # return JsonResponse(project_list, safe=False)

    def post(self, request):
        serializer = ProjectCreateAndUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectCreateAndUpdateSerializer(project, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


        # if serializer.is_valid():
            # name = serializer.validated_data['name']
            # description = serializer.validated_data['description']
            # project.name = name
        #     # project.description = description
        #     serializer.save()
        #     return Response(serializer.data,status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk=None):
        project= get_object_or_404(Project,pk=pk)
        project.delete()
        return Response({'message': 'Success!'})

class ProjectDetailTaskAPIView(APIView):
    def get(self, request, pk=None):
        tasks=Task.objects.filter(project_id=pk)
        serializers = TaskListSerializer(tasks, many=True)
        return Response(serializers.data)



# class TaskAPIView(APIView):
#     def get(self,request):
#        tasks=Task.objects.all()
#        serializers=TaskListSerializer(tasks,many=True)
#        return Response(serializers.data)
#
#
#     def post(self,request):
#         serializers=TaskCreateAndUpdateSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
# class TaskApiView(APIView):
#     def get(self,request):
#         tasks = Task.objects.all()
#         serializers = TaskListSerializer(tasks, many=True)
#         return Response(serializers.data)
#     def post(self,request):
#         serializers = TaskCreateAndUpdateSerializer(data=request.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response(serializers.data, status=status.HTTP_201_CREATED)
#     #     if serializers.is_valid():
#     #         serializers.save()
#     #         return Response(serializers.data, status=status.HTTP_201_CREATED)
#
#
# class TaskDetailApiView(APIView):
#     def get(self, request, pk=None):
#         tasks = get_object_or_404(Task,pk=pk)
#         serializers = TaskListSerializer(tasks, many=True)
#         return Response(serializers.data)
#
#     def put(self,request,pk=None):
#         task=get_object_or_404(Task,pk=pk)
#         serializers=TaskCreateAndUpdateSerializer(instance=task,data=request)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response(serializers.data,status=status.HTTP_200_OK)
#
#     def delete(self,request,pk=None):
#         task=get_object_or_404(Task,pk=pk)
#         task.delete()
#         return Response({'message':'Success'})




# class TaskViewSet(ViewSet):
#     def list(self,request):
#         tasks=Task.objects.all()
#         serializers=TaskListSerializer(tasks,many=True)
#         return Response(serializers.data)
# tasklarni ro'yxat
#
#     def retrieve(self,request,pk=None):
#         tasks=get_object_or_404(Task,pk=pk)
#         serializers=TaskListSerializer(tasks)
#         return Response(serializers.data)
#  1idni batavsil malumoti
#
#     def create(self,request):
#         serializers=TaskCreateAndUpdateSerializer(data=request.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response(serializers.data,status=status.HTTP_200_OK)
#post yaratmoqchi bo'lsak
#
#     def update(self,request,pk=None):
#         task=get_object_or_404(Task,pk=pk)
#         serializers=TaskCreateAndUpdateSerializer(instance=task,data=request)
#         serializers.is_valid()
#         return Response(serializers.data,status=status.HTTP_200_OK)
#o'zgartirish
#
#     def destroy(self,request,pk=None):
#         task=get_object_or_404(Task,pk=None)
#         task.delete()
#         return Response({'message': 'Success'})
# delett qilish


class TaskModelViewSet(ModelViewSet):
    queryset = Task.objects.all()
    # task model ichidagi hamma createlarni update qilamn
    serializer_class=TaskListSerializer

    def get_serializer_class(self):
        if self.action in ('create','update'):
            return TaskCreateAndUpdateSerializer
        else:
            return TaskListSerializer

    @action(detail=True, methods=['get'])
    def project_tasks(self, request, pk=None):
        tasks = Task.objects.filter(project_id=pk)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)
    @action(methods=['patch'],detail=True)
    def change(self,request,pk=None):
        task=get_object_or_404(Task,pk=pk)
        serializer=TaskCreateAndUpdateSerializer(instance=task,data=request.data,partial=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

