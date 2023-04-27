import os
from django.http import HttpResponse
from django.shortcuts import render
from google.cloud import storage
from django.conf import settings
from .forms import UploadForm
import re

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials-project2.json'

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded file
            uploaded_file = request.FILES['file']
            if uploaded_file.name.endswith('.zip'):
                # Upload the file to Google Cloud Storage
                storage_client = storage.Client()
                bucket = storage_client.bucket(settings.GS_BUCKET_NAME)
                blob = bucket.blob('Packages/' + uploaded_file.name)
                blob.upload_from_file(uploaded_file)
                # Redirect to a success page
                return render(request, 'success.html')
            else:
                # Display an error message if the file extension is not "zip"
                form.add_error('file', 'Only ZIP files are allowed.')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})

def file_list(request):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(settings.GS_BUCKET_NAME)
    blobs = bucket.list_blobs()
    file_names = [blob.name for blob in blobs]
    regex_pattern = re.compile(r'^Packages/[^/]+$')
    new_list = list(filter(regex_pattern.match, file_names))
    file_names = sorted(new_list)
    return render(request, 'list_files.html',  {'file_names': file_names})

def file_detail(request, filename):
    return render(request, 'file_detail.html', {'filename': filename})

def download_file(request):
    project_id = settings.GS_PROJECT_ID 
    bucket_name = settings.GS_BUCKET_NAME 
    
    if request.method == 'POST':
        blob_name = request.POST.get('file_name')
        # download the file using the file_name variable
        client = storage.Client(project_id)
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        response = HttpResponse(blob.download_as_bytes(), content_type=blob.content_type)
        response['Content-Disposition'] = f'attachment; filename="{blob_name}"'
        return response
    else:
        return HttpResponse("Invalid request method.")