from django.db import models

class Drawing(models.Model):
    image = models.ImageField(upload_to='drawings/')

    def __str__(self):
        return self.image.url[18:]