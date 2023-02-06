from django.db import models

# Create your models here.

class Human(models.Model):
    fname = models.CharField('Human first name', max_length=50)
    lname = models.CharField('Human last name', max_length=50)
    age = models.IntegerField('Human age')

    def __str__(self):
        return self.fname

    class Meta:
        # verbose_name_plural = 'Mardiqqqqqq'
        ordering = ['-fname']