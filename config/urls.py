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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path

# app별로 url관리

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # blog관련 path
    path('',include('blog.urls')),

    # portfolio 관련 path
    path('portfolio/',include('portfolio.urls')),
    
    #users관련 path
    path('users/',include('users.urls')),

    #member관련 path
    path('member/',include('member.urls')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    # 새로넣음

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# <int--:이름> = <type:name> 여러객체를 위한 계층적 url을 다루기 위해서 사용함.
