from django.db import models
from django.contrib.auth.models import User
    

class App(models.Model):
    id = models.AutoField(primary_key=True)
    html = models.TextField(blank=True)
     
    def __str__(self):
        return f"App {str(self.id)}" 