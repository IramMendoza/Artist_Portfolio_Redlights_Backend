from rest_framework import serializers
from .models import Artist, Contact, Member
from event.models import Picture
from event.serializers import EventSerializer, PictureSerializer

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        

class ArtistInfoSerializer(serializers.ModelSerializer):

    members = MemberSerializer(many=True, required=False)
    
    contact = ContactSerializer(required=False)
    
    class Meta:
        model = Artist
        fields = ['name', 'slogan', 'about', 'image', 'contact', 'members']

class ArtistPictureSerializer(serializers.ModelSerializer):
    
    pictures = PictureSerializer(many=True, required=False)
    
    class Meta:
        model = Artist
        fields = ['name', 'pictures']