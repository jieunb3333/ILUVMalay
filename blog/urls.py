from django.urls import path
import blog.views

app_name='blog'

urlpatterns = [
    path('',blog.views.index,name="index"),
    path('detail/<int:blog_id>/', blog.views.detail, name='detail'),
    path('create/', blog.views.create, name='create'),
    path('delete/<int:blog_id>/',blog.views.delete,name='delete'),
    path('update/<int:blog_id>/',blog.views.update,name='update'),
    path('information/',blog.views.information,name='information'),
]