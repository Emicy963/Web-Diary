from django.db import models

class People(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='picture')

    def __str__(self):
        return self.name
    

class Diary(models.Model):
    title = models.CharField(max_length=100)
    tags = models.TextField()
    text = models.TextField()
    people = models.ManyToManyField(People, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
