from django.db import models

# Create your models here.

class Current_Active_Users(models.Model):
    username=models.CharField(max_length=100)
    selected_topic=models.CharField(max_length=200)

    def __str__(self):
        return self.username
    
