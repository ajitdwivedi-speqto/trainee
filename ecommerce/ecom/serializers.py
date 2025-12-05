from rest_framework import serializers
from ecom.models import product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        # fields = '__all__'
        fields = ['id', 'name', 'price', 'specifications']    
