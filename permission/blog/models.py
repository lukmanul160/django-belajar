from django.db import models
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


class Artikel(models.Model):
    judul = models.CharField(max_length=255)
    isi = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    created = models.DateTimeField(auto_now_add = True)
    is_published = models.BooleanField(null=False)
    published = models.DateTimeField(null=True)

    class Meta:
        default_permissions = ('add',)
        permissions = (
            ('can_publish', 'can publish artikel'),
            ('can_edit', 'can edit artikel')
        )

    def save(self):
        self.slug = slugify(self.judul)

        print(self.is_published)
        if self.is_published == True :
            self.published = timezone.now()
        else:
            self.published = None

        super().save()

    def __str__(self):
        return "{}.{}".format(self.id, self.judul)
