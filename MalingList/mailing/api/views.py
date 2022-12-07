from rest_framework import generics, viewsets
from rest_framework.decorators import action

from mailing.api.serializers import *


class ClientAPIList(viewsets.ModelViewSet):
    def get_queryset(self):
        return Client.objects.all()

    serializer_class = ClientSerialzier
    http_method_names = ["get", "post"]


class MessageAPIList(viewsets.ModelViewSet):
    def get_queryset(self):
        return Message.objects.all()

    serializer_class = MessageSerializer
    http_method_names = ["get", "post"]


class MailingAPIList(viewsets.ModelViewSet):
    def get_queryset(self):
        return Mailing.objects.all()

    serializer_class = MailingSerializer
    http_method_names = ["get", "post"]