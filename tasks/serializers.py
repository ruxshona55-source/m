from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework import serializers
from tasks.models import Project, Task


class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    owner = UserSerializer()
#
# class ProjectList(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     owner = UserSerializer(many=True, read_only=True)


class ProjectCreateAndUpdateSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField()
    # description = serializers.CharField()
    # owner = UserSerializer()
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'owner')
    def validate(self,date):
        name=date.get('name')
        description=date.get('description')
        if name == description:
            raise serializers.ValidationError('Name and description cannot be same')
        return date


    def validate_name(self,value):
        if len(value) < 3:
            raise serializers.ValidationError('Name cannot be empty')
        return value
    # def create(self,validated_data):
    #     # name = validated_data['name']
    #     # description = validated_data['description']
    #     # project = Project.objects.create(name=name, description=description)
    #     # return project
    #     return Project.objects.create(**validated_data)
    #
    # def update(self,instance,data):
    #     # name=data.get('name')
    #     # description=data.get('description')
    #     # instance.name = name
    #     # instance.description = description
    #     # instance.save()
    #     # return instance
    #     Project.objects.filter(id=instance.id).update(**data)
    #     return Project.objects.get(id=instance.id)

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description')
class TaskCreateAndUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'to_user')
        extra_kwargs = {'id':{'read_only':True}}




