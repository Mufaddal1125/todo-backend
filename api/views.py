from rest_framework.views import APIView, Response
from api.models import Todo
from api.serializers import TODOSerializer

# Create your views here.

class TodoListView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TODOSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TODOSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=201)

class TodoView(APIView):
    def put(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        serializer = TODOSerializer(todo, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data)
