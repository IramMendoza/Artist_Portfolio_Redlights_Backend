from django.contrib import admin
from django.urls import path
from django.urls import include
from artist.views import ArtistRetrieveAPIView, ArtistPicturesListAPIView, ArtistMembersListAPIView
from event.views import EventListView, EventDetailView, EventSummaryListView, EventPictureList, HeaderPicturesListAPIView, NextEventListView, EventListPaginationView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/artist/<name>/', ArtistRetrieveAPIView.as_view()),
    path('api/artist/<name>/header/', HeaderPicturesListAPIView.as_view()),
    path('api/artist/<name>/pictures/',ArtistPicturesListAPIView.as_view()),
    path('api/artist/<name>/members/', ArtistMembersListAPIView.as_view()),
    path('api/artist/<artist>/events/<int:amount>', EventListView.as_view()),
    path('api/artist/<name>/events/pages/', EventListPaginationView.as_view()),
    path('api/artist/<artist>/events_summary/', EventSummaryListView.as_view()),
    path('api/artist/<name>/events/event/<int:id>/', EventDetailView.as_view()),
    path('api/artist/<name>/events/next_events/', NextEventListView.as_view()),
    path('api/artist/<name>/events/pictures/', EventPictureList.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)