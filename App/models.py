from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class File(models.Model):
    filename = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to="uploads")
    upload_date = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # permissions = models.ManyToManyField(User, related_name='files')
    
  

    def __str__(self):
        return self.filename



