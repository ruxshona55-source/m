from rest_framework import serializers
from tasks.models import Project


class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()

    def validate(self,date):
        name=date.get('name')
        description=date.get('description')
        if name == description:
            raise serializers.ValidationError('Name and description cannot be same')
        return date
