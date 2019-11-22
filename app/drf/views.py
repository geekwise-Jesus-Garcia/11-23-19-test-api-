from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from drf.serializer import User_Serializer, Group_Serializer


class User_Viewset(viewsets.ModelViewSet):
    """
    API endpoint that allows user to be viewes or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = User_Serializer

class Group_Viewset(viewsets.modelViewset):

    """
    API endpoint that allows group to be viewes or edited.
    """
    queryset = Group.objects.all()
    serializer_class = Group_Serializer
