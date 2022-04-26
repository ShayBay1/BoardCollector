from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('boards/', views.boards_index, name='index'),
    path('boards/<int:board_id>/', views.boards_details, name='detail'),
]