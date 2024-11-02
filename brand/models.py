from django.db import models

class BrandModel(models.Model):
    brand_name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40,unique=True)
    
    def __str__(self):
        return   self.brand_name