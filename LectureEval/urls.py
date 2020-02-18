from django.contrib import admin
from django.urls import path
import app.views
from app.views import GC2Read, LERead, PERead, WPRead #Read기능을 하는 ListView들 import하기


urlpatterns = [
    path('', app.views.index, name='main'),
    path('admin/', admin.site.urls, name="admin"),
    path('GC2/', GC2Read.as_view(), name='GC2'),
    path('LE/', LERead.as_view(), name='LE'),
    path('PE/', PERead.as_view(), name='PE'),
    path('WP/', WPRead.as_view(), name='WP'),
]

