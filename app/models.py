from django.db import models

# Create your models here.
class Like(models.Model):
    like = models.IntegerField(null=True)
    today = models.CharField(max_length=10, null = True)
