from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webpush', include('webpush.urls')),
    path('', include('BlogPost.urls')),

]
