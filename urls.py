from django.urls import path
from .controllers import views, media

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_post', views.submit_post, name='submit_post'),
    path('media_detail', media.detail, name='media_detail'),
    path('upload_file_select', media.upload_file_select, name='upload_file_select'),
]