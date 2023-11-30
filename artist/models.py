from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    type_artist = models.CharField(max_length=100)
    slogan = models.TextField(blank=True)
    about = models.TextField(blank=True)
    image = models.ImageField(upload_to='artist_image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    contact = models.OneToOneField('Contact', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20)
    phone_2 = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.email

class Member(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='member_photo')
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='members')

    def __str__(self):
            return self.name 