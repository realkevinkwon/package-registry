from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from google.cloud import storage

# Create your views here.
def restart_registry(request):
    if request.method == 'POST' and request.POST.get('restart') == 'yes':
        # Delete GCP Files
        project_id = settings.GS_PROJECT_ID 
        bucket_name = settings.GS_BUCKET_NAME 
        client = storage.Client(project_id)
        bucket = client.get_bucket(bucket_name)
        
        count = 0
        for blob in bucket.list_blobs():
        # Delete each blob
            blob.delete()
            count += 1

        context = {'count': count}

        return render(request, 'restart_success.html', context)
    else:
        return render(request, 'restart.html')