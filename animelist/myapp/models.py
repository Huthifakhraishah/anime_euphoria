from django.db import models
import re 

class Users(models.Model):
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    role=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Animes(models.Model):
    title=models.CharField(max_length=45)
    desc=models.TextField()
    release_date=models.DateField()
    rating=models.IntegerField(default=0)
    user_id_a=models.ForeignKey(Users,related_name="u_anime",on_delete=models.CASCADE)
    fav_list=models.ManyToManyField(Users,related_name="liked_a",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    comment=models.TextField()
    user_id= models.ForeignKey(Users, related_name="u_comment", on_delete=models.CASCADE)
    anime_id=models.ForeignKey(Animes, related_name="a_comment", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    category=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
