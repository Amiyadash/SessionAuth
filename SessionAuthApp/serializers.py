from rest_framework import  viewsets,serializers
from .models import Stud
class StudSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stud
        fields=('roll','name','marks')