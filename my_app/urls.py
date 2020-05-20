from django.urls import path
from . import views
#a list -> basically tell that if someone types something empty then take them to home page
urlpatterns = [
    path('', views.home, name='home'),
    path('new_search', views.new_search, name='new_search'),
]