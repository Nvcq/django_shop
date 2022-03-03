from django.urls import path, re_path
from . import views

app_name = 'caprisun'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/update', views.update, name='update'),
    path('<int:question_id>/delete', views.delete, name='delete'),


]