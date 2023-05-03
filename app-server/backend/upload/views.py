import os
from django.http import HttpResponse
from django.shortcuts import render
from google.cloud import storage
from django.conf import settings
from .forms import UploadForm
from .models import Packagey
from .model_contents import getModelContents
from .rate import rate_func
import re
import io
# from upload import rate
# import rate
import zipfile
import json

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded file
            uploaded_file = request.FILES['file']
            #package_zipped = uploaded_file
            if uploaded_file.name.endswith('.zip'):
                try:
                    package_url = getURLfrompackage(uploaded_file)
                    print(package_url)
                    
                    # Upload the file to Google Cloud Storage
                    storage_client = storage.Client()
                    bucket = storage_client.bucket(settings.GS_BUCKET_NAME)
                    blob = bucket.blob('Packages/' + uploaded_file.name)
                    uploaded_file.seek(0)
                    blob.upload_from_file(uploaded_file)
                    # Redirect to a success page
                    return render(request, 'success.html')
                except:
                    print("Hey")
                #try: url = getURLfrompackage(uploaded_file)
                #except: form.add_error('file','Uploaded Package is not Viable')
                #try: rating = rate_func(url)
                #except: rating = -1
                #if(rating < 0.5):
                #    form.add_error('file','Uploaded Package is not High Enough Quality')
                #    return render(request, "failure.html")
                #else:
                # print("Got Here!")
<<<<<<< HEAD
                #try: url = getURLfrompackage(uploaded_file)
                #except: form.add_error('file','Uploaded Package is not Viable')
                #try: rating = rate_func(url)
                #except: rating = -1
                #print(rating)
                #if(rating < 0.5):
                #   form.add_error('file','Uploaded Package is not High Enough Quality')
                #   return render(request, "failure.html")
                #else:
=======
                try: name, url, repo_ver = getDatafrompackage(uploaded_file)
                except: form.add_error('file','Uploaded Package is not Viable')
                try: rating = rate_func(url)
                except: rating = -1
                print(rating)
                if(rating < 0.5):
                   form.add_error('file','Uploaded Package is not High Enough Quality')
                   return render(request, "failure.html")
                else:
>>>>>>> d706b602cea6c8a5fc5f1cc1dbcecd5a6a6cda37
                    # The Django package model requires repo name, ID, version, popularity, and overall metric score
                    # Retrieve repository name, ID, and popularity
                #   [repo_name, repo_ID, stargazers, downs] = getModelContents(url)
                    # Attempt to retrieve version number
<<<<<<< HEAD
                #   try: repo_ver = getVersionfrompackage(uploaded_file)
                #   except: form.add_error('file', 'Uploaded Package does not contain version in json file')
=======
                #    try: repo_ver = getVersionfrompackage(uploaded_file)
                #    except: form.add_error('file', 'Uploaded Package does not contain version in json file')
>>>>>>> d706b602cea6c8a5fc5f1cc1dbcecd5a6a6cda37
                # Create model
                # upload_model = Packagey.objects.create(pack_name = str(repo_name), pack_ID = int(repo_ID), version_field = str(repo_ver), stars = int(stargazers), downloads = int(downs),  metrics_score = float("{:.2f}".format(rating)))
                # Upload model to Google Cloud Storage
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
    query = request.GET.get('q')
    if query:
        regex_pattern = re.compile(query)
        file_names = list(filter(regex_pattern.search, file_names))

    return render(request, 'list_files.html', {'file_names': file_names})

def hello_world(request):
    file_name = request.POST.get('file_name')
    return render(request, 'file_view.html', {'file_name': file_name})

def file_view(request, file_name):
    return render(request, 'file_view.html', {'file_name': file_name})

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
<<<<<<< HEAD

def get_package_json(zipped):
    print("2")
    with zipfile.ZipFile(zipped) as zip_file:
        if('package.json' in zip_file.namelist()):
            print("3")
            zip_file.extract('package.json')
            #with zip_file.open("package.json") as json_file:
            #    print("4")
            #    json_file_contents = json.load(json_file)
            #    print("5")
            #    return json_file_contents

def getURLfrompackage(zipped):
    folder_string = zipped.name.rstrip(".zip")
    with zipfile.ZipFile(zipped.file, 'r') as zip_file:
        jsonData = zip_file.read(f"{folder_string}/package.json").decode()
        data = json.load(io.StringIO(jsonData))
        url = data['repository']['url']
        url = url[6:]
        url = url.rstrip(".git")
        return(url)

def getURLfrompackage(zipped):
=======
    
def getDatafrompackage(zipped):
>>>>>>> d706b602cea6c8a5fc5f1cc1dbcecd5a6a6cda37
    folder_string = zipped.name.rstrip(".zip")
    with zipfile.ZipFile(zipped.file, 'r') as zip_file:
        jsonData = zip_file.read(f"{folder_string}/package.json").decode()
        data = json.load(io.StringIO(jsonData))
        url = data['repository']['url']
        url = url[6:]
        url = url.rstrip(".git")
        url = "https://"+url
        version = data['version']
        name = data['name']
        return(name,url,version)
    

# def getVersionfrompackage(zipped):
#     folder_string = zipped.name.rstrip(".zip")
#     with zipfile.ZipFile(zipped.file, 'r') as zip_file:
#         jsonData = zip_file.read(f"{folder_string}/package.json").decode()
#         data = json.load(io.StringIO(jsonData))
#         version = data['version']
#         return(version)