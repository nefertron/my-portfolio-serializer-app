from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class IntroductionViewSet(viewsets.ModelViewSet):
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class ExperiencesViewSet(viewsets.ModelViewSet):
    queryset = Experiences.objects.all()
    serializer_class = ExperiencesSerializer

class LanguagesViewSet(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-id')
    serializer_class = MessageSerializer
