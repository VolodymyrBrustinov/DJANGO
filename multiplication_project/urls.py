from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('multiplication_table/', include('multiplication_table.urls')),
    path('', include('multiplication_table.urls')),
]
