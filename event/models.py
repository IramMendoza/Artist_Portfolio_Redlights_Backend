from django.db import models
from artist.models import Artist

class Event(models.Model):
    venue = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    description = models.TextField(max_length=300, blank=True)
    date = models.DateField()
    ticket_price  = models.IntegerField(blank=True)
    next_event = models.BooleanField(null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='events')
    
    def __str__(self):
        return self.venue + ' ' + str(self.date)
    
class Picture(models.Model):
    
    ENCLOSURE_CHOICES = [
        ('vertical', 'Vertical'),
        ('horizontal', 'Horizontal'),
        ('square', 'Square'),
    ]

    picture = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=120, default='The Redlights')
    enclosure = models.CharField(max_length=20, choices=ENCLOSURE_CHOICES)
    on_header = models.BooleanField(blank=True, default=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='pictures')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='pictures')
    
    def __str__(self):
        if self.event:
            return f'{self.event.venue} {self.event.date} {self.caption} {self.id}'
        else:
            return f'{self.artist.name} {self.caption} {self.id}'