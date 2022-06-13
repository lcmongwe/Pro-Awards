from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to='pics/',blank=True)
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True,null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    bio= models.CharField(max_length=500, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='pics/',blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user',null=True,blank=True)    
    poster = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='poster',null=True,blank=True)
    img_name = models.CharField(max_length=200, blank=True)
    img_url = models.URLField(max_length=200, blank=True,null=True)
    img_description = models.CharField(max_length=200,blank=True)
    date_posted = models.DateTimeField(auto_now_add=True,blank=True)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
    
    def __str__(self):
        return self.img_name




class Review(models.Model):
    RATING_CHOICES = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
    )

    design=models.IntegerField(choices=RATING_CHOICES,blank=True,null=True)
    usability=models.IntegerField(choices=RATING_CHOICES,blank=True,null=True)
    content= models.IntegerField(choices=RATING_CHOICES,blank=True,null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post',null=True,blank=True)
    

    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()

    def __str__(self):
        return self.post.img_name