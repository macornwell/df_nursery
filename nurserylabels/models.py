from django.db import models
from django.contrib.auth.models import User


class CultivarLabel:
    name = None
    species = None
    ripens = None


class PreviousLabelOrder(models.Model):
    previous_label_order_id = models.AutoField(primary_key=True)
    data = models.TextField()
    datetime = models.DateTimeField()
    user = models.ForeignKey(User)
