from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import WowClassSerializer, ItemSerializer
from .models import WowClass, Weapon


# Create your views here.
@api_view(['GET'])
def getClasses(request):
    classes = WowClass.objects.all()
    serializer = WowClassSerializer(classes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getItems(request):
    items = Weapon.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)