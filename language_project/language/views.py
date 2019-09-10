from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Language,Paradigm,Programmer
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
        
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    # permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #permission_classes = [IsAuthenticated|ReadOnly]



class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer