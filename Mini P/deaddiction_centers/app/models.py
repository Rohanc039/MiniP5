from django.db import models

class DeAddictionCenter(models.Model):
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    ngo_name = models.CharField(max_length=200)
    address = models.TextField()
    bed_capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.ngo_name} - {self.state} ({self.district})"


