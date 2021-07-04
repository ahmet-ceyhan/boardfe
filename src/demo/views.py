from django.shortcuts import render
from .models import Demo
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DemoSerializers
from .models import Demo
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class DemoViewSet(viewsets.ModelViewSet):
    serializer_class = DemoSerializers
    queryset = Demo.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
