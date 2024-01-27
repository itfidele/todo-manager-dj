from django.urls import path
from .views import HomeView,TaskCreateView,CategoryCreateView,TaskDetailView,TaskListView,TaskUpdateView,TaskDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('task/', TaskListView.as_view(), name='task-list'),
     path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task-edit'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-view'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
   
   
]