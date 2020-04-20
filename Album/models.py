from django.db import models


class Music(models.Model):
    cover_image = models.TextField(blank=True, null=True)
    artist = models.CharField(max_length=300, blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    label = models.CharField(max_length=300, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    catalogue_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

