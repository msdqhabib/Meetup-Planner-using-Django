from django.db import models
from PIL import Image


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'({self.name} - {self.address})'

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    #blank = True -> no value is provided
    #null = True -> null value will be stored in db 
    participant = models.ManyToManyField(Participant, blank=True, null=True)
    organizer_email = models.EmailField()
    date = models.DateField()

    #To work with images in django pillow library is used
    image = models.ImageField(upload_to='meetups')

    def __str__(self):
        return self.title
    
    # Override the save method of the model
    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path) # Open image

    #     # resize image
    #     if img.height > 300 or img.width > 300:
    #        output_size = (300, 300)
    #        img.thumbnail(output_size) # Resize image
    #        img.save(self.image.path) # Save it again and override the larger image
   