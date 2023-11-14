
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('sweet_market.urls')), 
    path('admin/', admin.site.urls),
]


