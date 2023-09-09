from django.db import models


# Create your models here.


class Artist(models.Model):
    gender_a = (
        ('male', 'Male'),
        ('female','Female'),
        ('other','Other')
    )
    profile_img = models.FileField(blank=True, null=True, upload_to='media/images')
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=16,choices=gender_a)
    age = models.PositiveSmallIntegerField(default=25)
    email = models.EmailField(default='example@gmail.com', blank=True, null=True)
    phone = models.CharField(max_length=19)
    about = models.TextField(default="Your about only", blank=True, null=True)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Song(models.Model):
    janr = (
        ('rap', 'Rap'),
        ('jazz', 'Jazz'),
        ('hiphop', 'HipHop'),
        ('national', 'national'),
        ('rock', 'Rock')
    )
    title = models.CharField(max_length=25)
    year = models.DateField(blank=True, null=True)
    ganre = models.CharField(max_length=15, choices=janr)
    artist = models.ManyToManyField(Artist, blank=True, null=True)

    def __str__(self):
        return self.title




    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=50)
    album_img = models.FileField(blank=True, null=True, upload_to='media/album_image')
    year = models.DateTimeField(default=2023)
    song = models.ManyToManyField(Song, blank=True, null=True)
    artist = models.ManyToManyField(Artist, blank=True, null=True)
    album_about = models.TextField(blank=True, null=True, default='About your album')

    def __str__(self):
        return self.title

