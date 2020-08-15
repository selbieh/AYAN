from rest_framework import serializers
from .models import Task

class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Task

class TaskReadSerializer (serializers.ModelSerializer):
    '''
    readonly paramter in Meta to make the class  faster
    using 2 serializer class make better performance and more easy to edit and read
    this serializer make both tasked and all linked tasks readable from both ids
    '''
    link_to=TaskWriteSerializer(read_only=True)
    tasks=TaskWriteSerializer(many=True,read_only=True,source='linked_tasks')
    class Meta:
        fields='__all__'
        model =Task
        read_only=fields