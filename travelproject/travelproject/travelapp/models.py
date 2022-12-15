from django.db import models

# Create your models here.
class travel(models.Model):
    heading=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pictures')

    desc=models.TextField()

    def __str__(self):
        return self.heading

class guide(models.Model):
    pic=models.ImageField(upload_to='guides')


class guide1(models.Model):
    pic1=models.ImageField(upload_to='guide')
    pic2 = models.ImageField(upload_to='guide')
    pic3 = models.ImageField(upload_to='guide')
    pic4 = models.ImageField(upload_to='guide')

class design(models.Model):
    pic=models.ImageField(upload_to='guides')


class designing(models.Model):
    head=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()


