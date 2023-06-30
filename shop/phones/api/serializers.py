from rest_framework import serializers
from ..models import Product, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['title', 'img']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        if instance.img:
            response['img'] = instance.img.url
        return response


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'price', 'images']

