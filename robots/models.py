from django.db import models


class Robot(models.Model):
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.model} {self.version}"