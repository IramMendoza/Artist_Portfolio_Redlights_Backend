from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import EventSerializer, EventSummarySerializer, PictureSerializer, PicturePagination, PictureHeaderPagination, PictureListSerializer, EventPagination
from .models import Event, Picture
from django.http import Http404
from django.shortcuts import get_object_or_404
import random

class EventListView(ListAPIView):
    serializer_class = EventSerializer
    lookup_url_kwarg = 'artist'
    
    def get_queryset(self):
        amount = self.kwargs['amount']
        artist = self.kwargs['artist']
        event_list = list(Event.objects.filter(artist__name=artist, next_event=False))
        random.shuffle(event_list)
        return event_list[:amount]
    
class EventListPaginationView(ListAPIView):
    serializer_class = EventSerializer
    pagination_class = EventPagination
    lookup_field = 'name'

    def get_queryset(self):
        artist_name = self.kwargs['name']
        return Event.objects.filter(artist__name=artist_name, next_event=False)

class NextEventListView(ListAPIView):
    serializer_class = EventSerializer
    lookup_field = 'artist'
    
    def get_queryset(self):
        artist_name = self.kwargs['name']
        return Event.objects.filter(artist__name=artist_name, next_event=True)

class EventDetailView(RetrieveAPIView):
    serializer_class = EventSerializer
    lookup_url_kwarg = 'id'
    
    def get_object(self):
        event_id = self.kwargs['id']
        artist_name = self.kwargs['name']
        return get_object_or_404(Event, id=event_id, artist__name=artist_name)
    
class EventSummaryListView(ListAPIView):
    serializer_class = EventSummarySerializer
    lookup_field = 'artist'
    
    def get_queryset(self):
        artist = self.kwargs['artist']
        return Event.objects.filter(artist__name=artist)
    
class EventPictureList(ListAPIView):
    serializer_class = PictureSerializer
    pagination_class = PicturePagination
    lookup_field = 'name'
    
    def get_queryset(self):
        artist_name = self.kwargs['name']
        return Picture.objects.filter(event__artist__name=artist_name)
    
class HeaderPicturesListAPIView(ListAPIView):
    serializer_class = PictureListSerializer
    lookup_field = 'name'
    
    def get_queryset(self):
        artist_name = self.kwargs['name']
        picture_list = list(Picture.objects.filter(artist__name=artist_name, on_header=True))
        random.shuffle(picture_list)
        picture_list = picture_list[:15]
        list_1 = []
        list_2 = []
        list_3 = []
        for picture in picture_list :
            if len(list_1) <= 4 :
                list_1.append(picture)
            elif len(list_2) <= 4 :
                list_2.append(picture)
            else :
                list_3.append(picture)
        picture_list = [list_1,list_2,list_3]
        random.shuffle(picture_list)
        return picture_list

