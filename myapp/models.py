from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArticleManager(models.Manager):
    def create_article(self, name):
        article = self.create(article_name = name)
        return article

class Article(models.Model):
    article_name = models.CharField(max_length=100)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField()

    objects = ArticleManager()
'''
    def __str__(self):
        return self.data
'''