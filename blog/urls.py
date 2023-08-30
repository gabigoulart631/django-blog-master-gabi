from django.urls import path

from blog.views import index, ola

urlpatterns = [
    path('index/', index, name="index"),
    path('ola/', ola, name="ola"),
    path('posts/all', ola, name="posts_list"), # a view responsável é ola()
]