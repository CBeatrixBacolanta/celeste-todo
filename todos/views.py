from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def list(self, request, *args, **kwargs):
        print("List endpoint called")  # Debug log
        return super().list(request, *args, **kwargs)   