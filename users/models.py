from django.db import models
from django.contrib.auth.models import User

# importing Image from Pillow
from PIL import Image

# existing user method does not provide for profile
# create a new profile model by extending User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    
    # dunder str method will display how we want it to display
    # otherwise it will only display profile object if we dont create and use this method to display profile
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        
