from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes


def hello(request):
    if request.method =="GET":
        return HttpResponse("Welcome to Email Sender")



@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def mypage(request):
    if request.method == "POST":
        data = request.data
        name = data['name']
        return HttpResponse("HI {} ".format(name))
        
