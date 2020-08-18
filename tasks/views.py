from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serilaizers import TaskWriteSerializer,TaskReadSerializer
class TaskViewSet (ModelViewSet):
    queryset = Task.objects.all()

    def update(self, request, *args, **kwargs):
        task =self.get_object()
        if task and task.state == 'new':
            if request.data.get('link_to',None) == None:
                return Response({"error": "this task not in progress to link to other "}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return super(TaskViewSet,self).update(request, *args, **kwargs)
        if task and task.state == 'in_progress':
            if request.data.get('title',None) !=None or request.data.get('description',None) != None:
                return Response({"error": "this task available to be link with other task only"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return super(TaskViewSet,self).update(request, *args, **kwargs)
        if task and task.state == 'done':
            return Response({"error":"this task done can not be manipulated"},status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.request.method =='GET':
            return TaskWriteSerializer
        else:
            return TaskReadSerializer