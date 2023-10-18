from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(default='Anarka(default)', max_length=200, null=True)
#     desc_text = 'Hi, this is default description and you can change it'
#     desc = models.CharField(default=desc_text, max_length=200, null=True)
#     image = models.ImageField(upload_to='profile_pics', default='default.jpg', null=True, blank=True)
#     def _str_(self):
#         return f'{self.user.username} Profile'


class ExampleModel(models.Model):
    image_field = models.ImageField(upload_to="images/")
    file_field = models.FileField(upload_to="files/")

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='ddd')
    city = models.CharField(max_length=100, default='dd')
    website = models.URLField(default='dd.com')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', null =True , blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
# class User(models.Model):
#     # first_name = models.CharField(max_length=50)
#     # last_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=200, unique=True)
#     username = models.CharField(max_length=200, unique=True)
#     password1 = models.CharField(max_length=50)
#     password2 = models.CharField(max_length=50)
    
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.email
    
# class User(models.Model):
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     email = models.EmailField(max_length=200, unique=True)
#     username = models.CharField(max_length=200, unique=True)
#     password1 = models.CharField(max_length=50)
#     password2 = models.CharField(max_length=50)
    

#     def __str__(self):
#         return self.email
    
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'



    

class Ticket(models.Model):
    # img = models.TextField('image')
    company = models.CharField(max_length=70, help_text='Company name')
    city1 = models.CharField(max_length = 50, help_text='The name of city, which you are leaving')
    city2 = models.CharField(max_length = 50, help_text='The name of city, where you are arriving')
    time1 = models.DateTimeField(help_text='Time of leaving city1')
    time2 = models.DateTimeField(help_text='Time of arriving at city2')
    price = models.IntegerField(help_text='The price of your ticket')

    def __str__(self):
         return f"{self.company} ({self.city1} to {self.city2})"
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'



