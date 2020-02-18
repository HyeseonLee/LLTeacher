from django.contrib import admin
from django.urls import path
import app.views
from app.views import GC2Read #Read기능을 하는 ListView들 import하기


urlpatterns = [
    path('', app.views.index, name='main'),
    path('GC2/', GC2Read.as_view(), name='GC2'),
    path('admin/', admin.site.urls, name="admin"),
]
