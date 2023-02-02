from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from services.paginations import CustomPagination
from .filters import TodoFilter
from django_filters.rest_framework.backends import DjangoFilterBackend



class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.order_by("-created_at")
    serializer_class = TodoSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, )
    filterset_class = TodoFilter
    
    def perform_create(self, serializer):
        return serializer.save(status=False)



class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.order_by("-created_at")
    serializer_class = TodoSerializer
    lookup_field = "slug"