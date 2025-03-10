from django.db import models
from django.contrib.auth.models import User  # Import the User model

class Tape(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add foreign key to User

    def __str__(self):
        return self.title