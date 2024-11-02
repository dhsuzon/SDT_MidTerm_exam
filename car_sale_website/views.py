from django.shortcuts import render
from car.models import CarModel
from brand.models import BrandModel
from django.contrib.auth.decorators import login_required

def home(request,carbrand_slug = None):
   cars = CarModel.objects.all()
   if carbrand_slug is not None:
       brand = BrandModel.objects.get(slug=carbrand_slug)
       cars = cars.filter(brand=brand)
   brand = BrandModel.objects.all()
   return render(request, 'home.html',{'cars': cars, 'brand':brand})




