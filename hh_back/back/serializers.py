from rest_framework import serializers

from back.models import Tour, About

from rest_framework import serializers

from back.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    banner = serializers.URLField(source="userprofile.banner", allow_blank=True)
    photo = serializers.URLField(source="userprofile.photo", allow_blank=True)
    desc = serializers.CharField(source="userprofile.desc", allow_blank=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'banner', 'photo', 'email', 'desc']

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        if User.objects.get(id=instance.id):
            profile = User.objects.get(id=instance.id)
            profile_data = validated_data

            profile.banner = profile_data.get('banner', profile.banner)
            profile.photo = profile_data.get('photo', profile.photo)
            profile.desc = profile_data.get('desc', profile.desc)
            profile.save()
        else:
            User.objects.create(user=instance)

        return instance


class TourSerializer(serializers.Serializer):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    country = models.CharField(max_length=300)
    price = models.IntegerField()
    image = models.URLField(blank=True)


    def create(self, validated_data):
        tour = Tour.objects.create(name=validated_data.get('name','description','country','price','image'))
        return tour

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class CommentSerializer(serializers.Serializer):
    rating = serializers.IntegerField(read_only=True)
    text = serializers.CharField()

    def create(self, validated_data):
        comment = Comment.objects.create(email=validated_data.get("rating"),
                                           content=validated_data.get("text"))
        return comment

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('name', 'description', 'image', 'address', 'id')

    def create(self, validated_data):
        about = About.objects.create(name=validated_data['name'])
        return about

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()
        return instance
