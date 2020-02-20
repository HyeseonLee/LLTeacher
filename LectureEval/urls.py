from django.contrib import admin
from django.urls import path
import app.views
from app.views import GC2Read, LERead, PERead, WPRead #Read기능을 하는 ListView들 import하기
from app.views import GC2Create


urlpatterns = [
    path('', app.views.index, name='main'),
    path('admin/', admin.site.urls, name="admin"),
    path('GC2/', GC2Read.as_view(), name='GC2'),
    path('LE/', LERead.as_view(), name='LE'),
    path('PE/', PERead.as_view(), name='PE'),
    path('WP/', WPRead.as_view(), name='WP'),
    path('login/',app.views.login, name ='login'),
    path('signup/',app.views.signup , name = 'signup'),
    path('loginhome/',app.views.loginhome, name='loginhome'),
    path('GC2/create', GC2Create.as_view(), name="GC2_CREATE"),

    #path('GC2/create', GC2Create.as_view(), name="GC2_CREATE")
    #path('GC2/update/<int:pk>', GC2Update.as_view(), name="GC2_UPDATE")
    #path('GC2/delete/<int:pk>', GC2Delete.as_view(), name="GC2_DELETE")
]

