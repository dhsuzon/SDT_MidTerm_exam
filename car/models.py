from django.db import models
from brand.models import BrandModel


class CarModel(models.Model):
    Carname = models.CharField(max_length=40)
    carPrice =  models.IntegerField()
    CarDescription = models.TextField()
    CarImage = models.ImageField(upload_to='upload/')
    brand = models.ForeignKey(BrandModel,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    
    
    
    def __str__(self):
        return  self.Carname
    
    
class UserComment(models.Model):
    car = models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    commentText = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return F'name: {self.name} CommentText: {self.commentText}'
    
