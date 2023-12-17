from . import views
from django.urls import path

urlpatterns = [
    path('homepage', views.home, name='home'),
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
]
