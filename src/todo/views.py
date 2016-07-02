from django.shortcuts import render

# Create your views here.
from todo.models import TodoItem
from todo.serializers import TodoItemSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.decorators import list_route
from rest_framework.response import Response

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serialzer_class = TodoItemSerializer
    
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.url = reverse('todoitem-detail', args =[instance.pk], request=self.request)
        instance.save()
   
    def delete(self,request):
        TodoItem.object.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
