# mymap/models.py

# from django.db import models

# class Ministry(models.Model):
#     name = models.CharField(max_length=255)
#     type = models.CharField(max_length=50)
#     location = models.CharField(max_length=255)
#     lat = models.FloatField()
#     lng = models.FloatField()
#     description = models.TextField()
#     contact = models.EmailField()
#     website = models.URLField()

#     def __str__(self):
#         return self.name

from django.db import models

class Ministry(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    description = models.TextField()
    contact = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.name

# mymap/models.py

class Institution(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
