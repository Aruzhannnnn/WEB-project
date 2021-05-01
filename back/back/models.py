from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class User(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)

    banner = models.URLField(blank=True)
    photo = models.URLField(blank=True)
    desc = models.TextField(blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def to_json(self):
        return {
            'id': self.user.id,
            'username': self.user.username,
            # "password": self.user.check_password;
            "banner": self.banner,
            "photo": self.photo,
            "email": self.email,
            "desc": self.desc,
        }

    def __str__(self):
        return f'{self.user.username}#{self.id}'


class Tour(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    country = models.CharField(max_length=300)
    price = models.IntegerField()
    image = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Tours'
        verbose_name_plural = 'Tours'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address,
            'image': self.image
        }

    def __str__(self):
        return f'{self.id}: {self.name}'


class About(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField(default=0)
    description = models.CharField(max_length=400)
    address = models.CharField(max_length=300)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='guide')
    image = models.URLField(blank=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'tour': self.tour

        }


class Comment(models.Model):
    text = models.CharField(max_length=350)
    rating = models.IntegerField()
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def to_json(self):
        return {
            'text': self.id,
            'rating': self.name,
            'created_by': self.created_by
        }
