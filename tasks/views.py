

from rest_framework import status

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from tasks.models import Project
from tasks.serializers import ProjectSerializer


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
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            description = serializer.validated_data['description']
            project = Project(name=name, description=description)
            project.save()
            return Response({"message": " success"})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk=None):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            description = serializer.validated_data['description']
            project.name = name
            project.description = description
            project.save()
            return Response({'message': 'Success!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk=None):
        project= get_object_or_404(Project,pk=pk)
        project.delete()
        return Response({'message': 'Success!'})


