from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'mylist'

urlpatterns = [
    path('',  views.main, name='main'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload, name='upload'),
    path('upload_create/', views.upload_create, name='upload_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)