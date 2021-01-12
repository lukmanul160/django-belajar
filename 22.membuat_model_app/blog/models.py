from django.db import models
from django.utils.text import slugify
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.CharField(max_length=255,default="")
    slug = models.SlugField(blank=True,editable=False)

    def save(self):
        self.slug = slugify(self.title)
        super(Post,self).save()

    def __str__(self):
        return "{}.{}".format(self.id,self.title)
