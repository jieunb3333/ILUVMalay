"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.index,name="index"),
    path('detail/<int:blog_id>/', blog.views.detail, name='detail'),
    path('create/', blog.views.create, name='create'),
    path('delete/<int:blog_id>/',blog.views.delete,name='delete'),
    path('update/<int:blog_id>/',blog.views.update,name='update'),
    
    path('portfolio', portfolio.views.portfolio,name='portfolio'),
    path('portfolio_create', portfolio.views.portfolio_create,name='portfolio_create'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# <int--:이름> = <type:name> 여러객체를 위한 계층적 url을 다루기 위해서 사용함.
