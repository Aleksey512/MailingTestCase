from django.urls import path, include

from . import views

from .api.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'clients', ClientAPIList, basename='client')
router.register(r'messages', MessageAPIList, basename='message')
router.register(r'mailings', MailingAPIList, basename='mailing')

urlpatterns = [
    path('', views.home, name="Главная"),
]

urlpatterns += router.urls
