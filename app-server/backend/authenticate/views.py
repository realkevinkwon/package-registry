from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def auth_func(request):
    if(request.method == 'PUT' and request.content_type == 'application/json'):
        return JsonResponse({'message': 'This system does not support authentication.'}, status=501)
 