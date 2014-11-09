from django.db import models

# Create your models here.
class Urls(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=200)
    clicks = models.IntegerField()
    creation_date = models.DateTimeField(auto_now=True)
