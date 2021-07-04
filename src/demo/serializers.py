from rest_framework import serializers
from .models import Demo


class DemoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = ['text', 'number']
