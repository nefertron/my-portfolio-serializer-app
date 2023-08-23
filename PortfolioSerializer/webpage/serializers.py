from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class ExperiencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiences
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'




