from django.db import models
from django.contrib.auth.models import User

# Create your models here.





class File(models.Model):
    filename = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to="uploads/", blank=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)
 
    
    def __str__(self):
        return self.filename
    
    




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    files = models.ManyToManyField(File, related_name='users')
