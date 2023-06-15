from django.db import models


class Oil(models.Model):
    name = models.CharField(max_length=20)
    img_link = models.CharField(max_length=300)

    def __str__(self):
        return self.name