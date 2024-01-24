from django.db import models


class MultiplicationTable(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)

    class Meta:
        app_label = 'multiplication_table'
