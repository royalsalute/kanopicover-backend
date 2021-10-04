from django.db import models


class ColorSpace(models.Model):
    name = models.CharField(max_length=16, unique=True)


class ColorSpaceField(models.Model):
    name = models.CharField(max_length=16)
    min_value = models.IntegerField()
    max_value = models.IntegerField()
    space = models.ForeignKey(ColorSpace, on_delete=models.CASCADE, related_name='fields')

    class Meta:
        unique_together = (('space_id', 'name'), )

