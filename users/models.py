from django.db import models

from companies.models import Division


class Employee(models.Model):
    nik = models.CharField(max_length=30, unique=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='divisions')
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.nik

    class Meta:
        db_table = 'employee'
