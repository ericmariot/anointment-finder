from anointments.managers import AnointmentManager
from django.db import models
from oils.models import Oil


class Anointment(models.Model):
    name = models.CharField(max_length=20)
    img_link = models.CharField(max_length=300)
    description = models.TextField()
    oil_1 = models.ForeignKey(Oil, related_name="oil_1", on_delete=models.CASCADE)
    oil_2 = models.ForeignKey(Oil, related_name="oil_2", on_delete=models.CASCADE)
    oil_3 = models.ForeignKey(Oil, related_name="oil_3", on_delete=models.CASCADE)

    objects = AnointmentManager()

    @property
    def oils(self):
        return [self.oil_1, self.oil_2, self.oil_3]

    def __str__(self):
        return self.name
