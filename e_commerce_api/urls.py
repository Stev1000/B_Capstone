from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('E_commerce.urls')),  # Ensure the case matches your app folder name
]
