from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250)
    Description = models.TextField()
    Date = models.DateField()


    def __str__(self):
        return self.title
