from django.db import models
from django.contrib.auth.models import User
    

class App(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='app_images', blank=True, null=True)
    
    
    def __str__(self):
        return self.name