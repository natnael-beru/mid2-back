from django.db import models

# Create your models here.
class techclass(models.Model):
       name=models.CharField(max_length=23)
       def __str__(self):
        return self.name