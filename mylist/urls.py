from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'mylist'

urlpatterns = [
    path('',  views.main, name='main'),
    path('write',  views.write, name='write'),
    path('modify<int:list_id>',  views.modify, name='modify'),
    path('detail<int:list_id>',  views.detail, name='detail'),
    path('delete<int:list_id>',  views.delete, name='delete'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload, name='upload'),
    path('upload_create/', views.upload_create, name='upload_create'),
    path('upload_modify<int:list_id>', views.upload_modify, name='upload_modify'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)