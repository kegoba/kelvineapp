from rest_framework import serializers
from .models import Record2

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record2
        read_only_fields =["id"]
        fields = ["id", "name","product", "amount", "description"]
      