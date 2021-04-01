#THIS WILL BE THE MAIN APP


from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.app, name="app"),  
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
]


