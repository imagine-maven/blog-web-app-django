from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Django follows the DRY Principle. The goal is to define your data model in one place and automatically derive things from it.

# your models are essentially your database layout, with additional metadata

# Post model -- inherits from django Model class
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={ 'pk': self.pk })

    
    
    
    
