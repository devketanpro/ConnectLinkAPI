from django.db import models

from user_app.models import User

class Interest(models.Model):
    sender = models.ForeignKey(User, related_name='sent_interests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_interests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    participants = models.ManyToManyField(User)
