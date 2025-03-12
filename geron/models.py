from django.db import models
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta

class Membership(models.Model):
    MEMBERSHIP_CHOICES = [
        ('1_month', '1 Месяц'),
        ('3_months', '3 Месяца'),
        ('6_months', '6 Месяцев'),
        ('1_year', '1 Год'),
    ]

    MEMBERSHIP_PRICES = {
        '1_month': 10000,
        '3_months': 30000,
        '6_months': 60000,
        '1_year': 110000,
    }
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_name = models.CharField(max_length=100)
    child_name = models.CharField(max_length=100)
    start_date = models.DateField()
    membership_type = models.CharField(
        max_length=10, choices=MEMBERSHIP_CHOICES, default='1_month'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    end_date = models.DateField(null=True, blank=True) 

    def save(self, *args, **kwargs):
        self.price = self.MEMBERSHIP_PRICES.get(self.membership_type, 10000)

        if self.start_date:
            if self.membership_type == '1_month':
                self.end_date = self.start_date + relativedelta(months=1)
            elif self.membership_type == '3_months':
                self.end_date = self.start_date + relativedelta(months=3)
            elif self.membership_type == '6_months':
                self.end_date = self.start_date + relativedelta(months=6)
            elif self.membership_type == '1_year':
                self.end_date = self.start_date + relativedelta(years=1)

        super(Membership, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.parent_name} - {self.child_name}"
