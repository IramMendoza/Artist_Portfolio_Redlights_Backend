from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import Artist, Member
from .serializers import ArtistInfoSerializer, ArtistPictureSerializer, MemberSerializer
from event.models import Picture
from event.serializers import PictureSerializer, PicturePagination
import random

class ArtistRetrieveAPIView(RetrieveAPIView):
    serializer_class = ArtistInfoSerializer
    lookup_field = 'name'

    def get_queryset(self):
        artist_name = self.kwargs['name']
        queryset = Artist.objects.filter(name=artist_name)
        return queryset

class ArtistPicturesListAPIView(ListAPIView):
    serializer_class = PictureSerializer
    pagination_class = PicturePagination
    lookup_field = 'name'
    
    def get_queryset(self):
        artist_name = self.kwargs['name']
        queryset = Picture.objects.filter(artist__name=artist_name)
        return queryset

class ArtistMembersListAPIView(ListAPIView):
    serializer_class = MemberSerializer
    lookup_field = 'name'

    def get_queryset(self):
        artist_name = self.kwargs['name']
        members_list = list(Member.objects.filter(artist__name=artist_name))
        random.shuffle(members_list)
        return members_list