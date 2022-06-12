from rest_framework import serializers
from .models import Post

class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','image' ,'img_name','img_url' ,'img_description')