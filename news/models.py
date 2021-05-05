
from django.db import models
from django.contrib.auth import get_user_model


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

User=get_user_model()
class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return '%i %s %s %s %s'%(self.id,self.title,self.description,self.author,self.tags)
