from rest_framework import serializers, pagination
from .models import Event, Picture

class PictureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Picture
        fields = '__all__'
        
class PictureHeaderPagination(pagination.PageNumberPagination):
    
    page_size = 15
    max_page_size = 100
    
class PicturePagination(pagination.PageNumberPagination):
    
    page_size = 6

class EventPagination(pagination.PageNumberPagination):

    page_size = 6

class PictureListSerializer(serializers.ListSerializer):
    
    child = PictureSerializer()

class EventSerializer(serializers.ModelSerializer):
    
    pictures = PictureSerializer(many=True, read_only=True)
    
    class Meta:
        model = Event
        fields = '__all__'

class EventSummarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ['id', 'venue', 'date', 'event_image']