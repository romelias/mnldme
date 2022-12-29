from .views import *
from django.urls import path
from .views import *
from  webapp import views
urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
    path('clips/', clips, name='clips'),
    path('services/', services, name='services')
]


