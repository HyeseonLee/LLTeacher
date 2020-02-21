from django.contrib import admin
from django.urls import path
import app.views
from app.views import GC2Read, LERead, PERead, WPRead, GC2Create, LECreate, PECreate, WPCreate, GC2Update, LEUpdate, PEUpdate, WPUpdate, GC2Delete, LEDelete, PEDelete, WPDelete

urlpatterns = [
    path('', app.views.index, name='main'),
    path('admin/', admin.site.urls, name="admin"),
    path('login/',app.views.login, name ='login'),
    path('logout/',app.views.logout, name='logout'),
    path('signup/',app.views.signup , name = 'signup'),
    path('loginPage/', app.views.loginPage, name='loginPage'),
    path('signupPage/', app.views.signupPage, name="signupPage"),
    path('mypage',app.views.mypage, name='mypage'),

    path('GC2/', GC2Read.as_view(), name='GC2'),
    path('GC2/create', GC2Create.as_view(), name="GC2_CREATE"),
    path('GC2/update/<int:pk>', GC2Update.as_view(), name="GC2_UPDATE"),
    path('GC2/delete/<int:pk>', GC2Delete.as_view(), name="GC2_DELETE"),

    path('LE/', LERead.as_view(), name='LE'),
    path('LE/create', LECreate.as_view(), name="LE_CREATE"),
    path('LE/update/<int:pk>', LEUpdate.as_view(), name="LE_UPDATE"),
    path('LE/delete/<int:pk>', LEDelete.as_view(), name="LE_DELETE"),

    path('PE/', PERead.as_view(), name='PE'),
    path('PE/create', PECreate.as_view(), name="PE_CREATE"),
    path('PE/update/<int:pk>', PEUpdate.as_view(), name="PE_UPDATE"),
    path('PE/delete/<int:pk>', PEDelete.as_view(), name="PE_DELETE"),

    path('WP/', WPRead.as_view(), name='WP'),
    path('WP/create', WPCreate.as_view(), name="WP_CREATE"),
    path('WP/update/<int:pk>', WPUpdate.as_view(), name="WP_UPDATE"),
    path('WP/delete/<int:pk>', WPDelete.as_view(), name="WP_DELETE"),
]

