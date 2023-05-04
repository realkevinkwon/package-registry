from django.urls import path
from .views import upload_file, download_file, file_list, file_view#, indv_package, indv_package_rate

urlpatterns = [
    # Path to view all files in the bucket
    path('upload', upload_file, name='upload_file'),
    path('packages/', file_list, name='file_list'),
    path('file_view/<filename>', file_view, name='file_view'),
    # path('download-file/', download_file, name='download_file'),
    # path(r"^upload/(?P<slug>[\w-]+)$",indv_package, name = 'individual-packages'), #change upload to package /package/{id}
    # path(r"^upload/(?P<slug>[\w-]+)/rate$",indv_package_rate, name = 'individual-ratings'), #change upload to package /package/{id}/rate
    #path('files/<str:blob_name>/', download_file, name='download_file'),
]