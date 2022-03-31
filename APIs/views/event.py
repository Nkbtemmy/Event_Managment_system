from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import status
# from APIs.serializers import EventSerializer
# from APIs.models import Events

# Create your views here.
@api_view(['GET'])
def defaults(request):
    return Response({"message":"Welcome to my homepage"})
