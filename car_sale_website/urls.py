
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/',include('car.urls')),
    # path('brand/',include('brand.urls')),
    path('',views.home,name="homepage"),
    path('carbrand/<slug:carbrand_slug>/',views.home,name="carbrand_homepage"),
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

