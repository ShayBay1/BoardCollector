from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('boards/', views.boards_index, name='index'),
    path('boards/<int:board_id>/', views.boards_detail, name='detail'),
    path('boards/create/', views.BoardCreate.as_view(), name ='boards_create'),
    path('boards/<int:pk>/update/', views.BoardUpdate.as_view(), name='boards_update'),
    path('boards/<int:pk>/delete/', views.BoardDelete.as_view(), name='boards_delete'),
    path('boards/<int:board_id>/add_tuning/', views.add_tuning, name='add_tuning'),
]
