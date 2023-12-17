from . import views
from django.urls import path

urlpatterns = [
    # path('homepage', views.home, name='home'),
    path('posts/', views.list_create, name='list_create'),
    path('posts/<int:id>', views.retrieve_update_delete, name='retrieve_update_delete'),
    # path('posts/<int:id>', views.update, name='update'),
    # path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    # path('posts/<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post-retrieve-update-delete'),
]
