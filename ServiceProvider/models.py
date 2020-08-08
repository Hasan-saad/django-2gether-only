from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from accounts.models import Profile


def image_upload(instance, fileName):
    imageName , extension = fileName.split(".")
    return "service/%s.%s"%(instance.id, extension)

class ServicProvider(models.Model):
    user = models.ForeignKey(User, related_name='service_provider', on_delete=models.CASCADE,default=1)
    # fName = models.CharField(max_length=100)
    # lName = models.CharField(max_length=100)
    jopType = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    publishAt = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    img = models.ImageField(upload_to=image_upload)
    Vacancy = models.IntegerField(max_length=None)
    # dateTime = models.DateTimeField(auto_now=False, auto_now_add=True)
    # slug = models.SlugField(blank=True, null=True)

    # def save(self ,*args,**kwargs):
    #     self.slug = slugify(self.jopType)
    #     super(ServicProvider, self).save(*args,**kwargs)


    def __str__(self):
        return str(self.user)

# class comments(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     commentOn = models.ForeignKey(ServicProvider, on_delete=models.CASCADE)
#     body = models.TextField(max_length=500)
#     publishAt = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.user.username)



class Category(models.Model):
    name = models.CharField(max_length=25)
    # img = models.ImageField(upload_to='Category/')
    # number_of_servic = models.IntegerField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    service = models.ForeignKey(ServicProvider, related_name='applyService', on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=11)
    descriptionProblem = models.TextField(max_length=100)
    applyAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.service)






class Comment(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='comments')
    serviceProvider = models.ForeignKey(ServicProvider,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)




