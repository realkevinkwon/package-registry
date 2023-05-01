from django.urls import path
from .views import upload_file, download_file, file_list, hello_world

urlpatterns = [
    # Path to view all files in the bucket
    path('upload', upload_file, name='upload_file'),
    path('packages/', file_list, name='file_list'),
    path('hello/', hello_world, name='hello_world'),
    path('download-file/', download_file, name='download_file'),

    #path('files/<str:blob_name>/', download_file, name='download_file'),
]