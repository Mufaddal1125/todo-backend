from api import views
from django.urls import path

urlpatterns = [
    path('todo', views.TodoListView.as_view(), name='todo'),
    path('todo/<int:pk>', views.TodoView.as_view(), name='todo'),
]
