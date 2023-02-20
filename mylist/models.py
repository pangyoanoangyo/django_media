from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    title = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='images/') #upload_to 옵션을 넣은 것은 BASE_DIR/images/아래에 저장해달라는 말입니다.
    
    def __str__(self):
        return self.title
    
class Profile_add(models.Model):
    title = models.CharField(max_length=200,null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    no_test=models.TextField()
    etc=models.TextField()
    error_1=models.TextField()
    error_2=models.TextField()
    error_3=models.TextField()
    error_4=models.TextField()
    error_content=models.TextField()
    error_fix=models.TextField()
    address=models.TextField()
    person1=models.TextField()
    person2=models.TextField()
    person_phone1=models.TextField()
    person3=models.TextField()
    person4=models.TextField()
    person_phone2=models.TextField()
    image = models.ImageField(upload_to='images/') #upload_to 옵션을 넣은 것은 BASE_DIR/images/아래에 저장해달라는 말입니다.
    
    def __str__(self):
        return self.title