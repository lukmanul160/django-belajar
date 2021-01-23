from django.db import models

# Create your models here.
class Instagram(models.Model):
    nama_depan      =  models.CharField(max_length=50)
    nama_belakang    = models.CharField(max_length=50)
    username         = models.CharField(max_length=50)
    content          = models.CharField(max_length=50)

    def __str__(self):
        return "{}.{}".format(self.id,self.username)