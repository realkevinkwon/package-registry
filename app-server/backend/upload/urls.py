from django.urls import path
from .views import upload_file, download_file, file_list, file_detail

urlpatterns = [
    # Path to view all files in the bucket
    path('upload', upload_file, name='upload_file'),
    path('', file_list, name='file_list'),
    path('file/<str:filename>/', file_detail, name='file_detail'),
    path('download-file/', download_file, name='download_file'),

    #path('files/<str:blob_name>/', download_file, name='download_file'),
]