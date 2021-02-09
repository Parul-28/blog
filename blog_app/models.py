from django.db import models

# Create your models here.
class Blog(models.Model):

    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='portfolio_app/images')
    description=models.CharField(max_length=200)
    url=models.URLField(blank= True)

    def __str__(self):
            return self.title
            # title as heading in admin page
