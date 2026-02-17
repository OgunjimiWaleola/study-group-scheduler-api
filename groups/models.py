from django.db import models
from django.contrib.auth.models import User

class StudyGroup(models.Model):
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)
    scheduled_date = models.DateTimeField()
    max_participants = models.IntegerField(default=10)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_groups"
    )
    participants = models.ManyToManyField(
        User, related_name="joined_groups", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
