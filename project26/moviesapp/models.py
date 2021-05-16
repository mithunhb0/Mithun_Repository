from django.db import models

# Create your models here.
class movietable(models.Model):
    moviename=models.CharField(max_length=20)
    hero=models.CharField(max_length=20)
    heroine=models.CharField(max_length=20)
   
    class Meta:
        verbose_name = 'movietable'
        verbose_name_plural = 'movietables'

    def __str__(self):
        return self.name
      
      
      
  