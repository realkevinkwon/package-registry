from django.shortcuts import render
from django.conf import settings
from google.cloud import storage
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
from rest_framework.request import Request
from django.http import HttpResponse
from .utils import generate_auth_token

@api_view(['GET','DELETE'])
def reset_registry(request: Request):
    # Check for X-Authorization header
    auth_token = request.META.get('HTTP_X_AUTHORIZATION')
    
    if not auth_token:
        return Response({'message': 'There is missing field(s) in the AuthenticationToken or it\
            \ is formed improperly, or the AuthenticationToken is invalid.'}, status=status.HTTP_400_BAD_REQUEST)
    
    project_id = settings.GS_PROJECT_ID 
    bucket_name = settings.GS_BUCKET_NAME 
    client = storage.Client(project_id)
    bucket = client.get_bucket(bucket_name)
        
    for blob in bucket.list_blobs():
        # Delete each blob
        blob.delete()

    return Response({'message': 'Registry is reset.'}, status=200)

@api_view(['GET', 'POST'])
def render_reset(request):
    if request.method == 'POST':
        reset_value = request.POST.get('reset')
        if reset_value == 'yes':
            drf_request = Request(request)
            reset_registry(drf_request)
            return render(request, 'reset_success.html')
        else:
            return render(request, 'reset_cancel.html')
    else:
        auth_token = generate_auth_token()
        context = {'auth_token': auth_token}
        return HttpResponse(render(request, 'reset.html', context))

def render_reset_success(request):
    return render(request, 'reset_success.html')
