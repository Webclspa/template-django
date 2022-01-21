from django.db import models
from PIL import Image

# Create your models here.

class Illustration(models.Model):
    title = models.CharField(max_length=255)
    illustration_slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title
