from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    # srno is created automatically as id
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)  # Adds current date/time automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.title}"
