from django.urls import path
from django.urls.conf import include
from .import views
urlpatterns = [
    path('test',views.testfun,name='test'),
    path('',views.welcomefun,name='welcome'),
    path('about',views.aboutfun,name='about'),
    path('contact',views.contactfun,name='contact'),

]