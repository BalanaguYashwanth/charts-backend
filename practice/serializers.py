from rest_framework import serializers
from .models import *

class addSerializer(serializers.ModelSerializer):
    class Meta:
        model=addition
        fields='__all__'

