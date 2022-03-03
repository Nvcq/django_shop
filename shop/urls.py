from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('<int:product_id>/update', views.update, name='update'),
    path('<int:product_id>/delete', views.delete, name='delete'),
]