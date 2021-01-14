from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"

class Post(models.Model):
    data = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="posts")
    timestamp = models.DateTimeField(default=None)
    def __str__(self):
        return f"{self.writer}: {self.data}"

class Like(models.Model):
    post = models.ManyToManyField(Post)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=False)
    pass

class Follow(models.Model):
    follower = models.ManyToManyField(User, related_name="others") 
    followed = models.OneToOneField(User, on_delete=models.CASCADE, default=None, related_name="users")
    pass
