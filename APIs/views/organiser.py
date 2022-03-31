from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from APIs.serializers import OrganiserSerializer
from APIs.models import Organisers, Events

# Create your views here.
@api_view(['GET'])
def default(request):
    return Response({"message":"Welcome to my homepage"})

@api_view(['GET'])
def organisersList(request):
    all_organisers = Organisers.objects.filter(deleted=False).all()
    serializer = OrganiserSerializer(all_organisers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def organiserDetails(request,pk):
    try:
        organiser = Organisers.objects.get(Organiser_id=pk)
        serializer = OrganiserSerializer(organiser, many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Organisers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data="organiser doesn't found")

@api_view(['POST'])
def addOrganiser(request):
    serializer = OrganiserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def updateOrganiser(request,pk):
    try:
        organiser = Organisers.objects.get(Organiser_id=pk)
    except Organisers.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND,data="organiser doesn't found")
    serializer = OrganiserSerializer(instance=organiser,data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteOrganiser(request,pk):
    try:
        organiser = Organisers.objects.filter(Organiser_id=pk).update(deleted=True)
        Response(data=organiser,status=status.HTTP_200_OK)
        # organiser.delete()
    except Organisers.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND,data="task doesn't found")
    return Response(status=status.HTTP_204_NO_CONTENT)
