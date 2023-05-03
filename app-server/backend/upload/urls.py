from django.urls import path
from .views import upload_file, download_file, file_list, file_view

urlpatterns = [
    # Path to view all files in the bucket
    path('upload', upload_file, name='upload_file'),
    path('packages/', file_list, name='file_list'),
    path('file_view/', file_view, name='file_view'),
    path('download-file/', download_file, name='download_file'),

    #path('files/<str:blob_name>/', download_file, name='download_file'),
]