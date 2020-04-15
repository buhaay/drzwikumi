from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('offer/maindoors', views.offer_main, name='offer_main'),
    path('offer/maindoors/<str:door_name>/', views.door_details, name='door_details'),
    path('offer/roomdoors', views.offer_room, name='offer_room'),
    path('offer/roomdoors/<str:door_name>/<str:door_series>', views.room_details, name='room_details'),
    path('offer/borderdoors', views.border_details, name='border_details'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    # path()
]
