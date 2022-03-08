from django.db import models

# Create your models here.


class Films(models.Model):
    STATUS_CHOICES = (
        (0, "New"),
        (1, "Old"),
    )

    name = models.CharField(max_length=30)
    rate = models.IntegerField()
    created_at = models.IntegerField()
    is_published = models.BooleanField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.created_at, self.rate)
