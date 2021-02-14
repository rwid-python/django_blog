"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from myblog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog_crud/', views.blog_create, name='blog_crud'),
    path('blog/<int:blog_id>/', views.blog, name='blog'),
    path('blog/<int:blog_id>/update', views.blog_update, name='blog_update'),
    path('blog/<int:blog_id>/delete', views.blog_delete, name='blog_delete'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('search/', views.search, name='search'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
