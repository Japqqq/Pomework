from django.db import models

class Playlist(models.Model):
    title = models.CharField(max_length= 200)
    fav = models.BooleanField(default = False)
    tag = models.CharField(max_length= 40)
    description = models.TextField(max_length= 2000)
    link = models.CharField(max_length=2000 , default='DEFAULT VALUE') 
    pic = models.ImageField(null = True , blank = True)
    def __str__(self):
        return self.title