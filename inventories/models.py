from django.db import models

from companies.models import Company
from users.models import Employee


class Inventory(models.Model):
    name = models.CharField(max_length=200)
    modeling = models.CharField(max_length=200, blank=True, null=True)
    stock = models.PositiveIntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='inventorycompany')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'inventory'


class Assign(models.Model):
    STATUS_OK = 'ok'
    STATUS_BACK = 'back'
    STATUS_FAIL = 'fail'

    STATUS_CHOICES = (
        (STATUS_OK, 'Ok'),
        (STATUS_BACK, 'Back'),
        (STATUS_FAIL, 'Fail'),
    )

    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='assigninventory')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='asiggnemployee')
    assigned = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assignassigned')
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_OK)
    flag_code = models.CharField(max_length=30, blank=True, null=True, unique=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.inventory.name

    class Meta:
        db_table = 'assign'
