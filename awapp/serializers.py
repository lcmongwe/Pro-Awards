from rest_framework import serializers
from .models import Post,Profile

class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','image' ,'img_name','img_url' ,'img_description')


class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','image' ,'name','phone' ,'email','bio')