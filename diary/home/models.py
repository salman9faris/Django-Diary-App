from django.conf import settings
from django.db import models
import datetime

# Create your models here.
class Diaryy(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=15)
    title=models.CharField(max_length=50)
    diary=models.TextField()
    user_name= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


