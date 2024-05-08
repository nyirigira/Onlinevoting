from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='candidates_pics/', blank=True, null=True)
    vote_count = models.IntegerField(default=0)  # Field to track vote count

    def __str__(self):
        return self.name
class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.voter.username} voted for {self.candidate.name}'
