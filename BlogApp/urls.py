from . import views
from django.urls import path

urlpatterns = [
    
    path('', views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),

]