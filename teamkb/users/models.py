from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField

# New model to store additional User information such as profile pic.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = RichTextField (blank=True, null = True)

    def __str__(self):
        return f'{self.user.username} Profile Page'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs) # Run the Parent class Save function 
        # when a new User is created, a linked profile record is also created.
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)