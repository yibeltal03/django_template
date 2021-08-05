from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length= 1000)
    #time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title