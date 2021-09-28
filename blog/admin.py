from django.contrib import admin
from .models import Post

# Register your models here.

# register model Post for admin page
admin.site.register(Post)