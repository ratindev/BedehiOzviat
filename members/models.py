from django.db import models

class Membership(models.Model):
    Name = models.CharField(max_length=255, verbose_name="نام")
    Family = models.CharField(max_length=255, verbose_name="نام خانوادگی")
    codemeli = models.CharField(unique=True, max_length=255, verbose_name="کد ملی")
    year = models.IntegerField(unique=False, verbose_name="سالهای عضویت")
    
    def calculate_amount(self):
        if self.year == 1382 or self.year == 1383 or self.year == 1384 or self.year == 1385 or self.year == 1386 or self.year == 1387 or self.year == 1388 or self.year == 1389 or self.year == 1390 or self.year == 1391 or self.year == 1392 or self.year == 1393 or self.year == 1394 or self.year == 1395 or self.year == 1396:
            return 25000
        elif self.year == 1397:
            return 50000
        elif self.year == 2018 or self.year == 2019:
            return 70000
        elif self.year == 1400:
            return 100000
        elif self.year == 1401:
            return 150000
        elif self.year == 1402:
            return 200000
        else:
            return 0  # Default to 0 if the year is not specified

    def __str__(self):
        return f"{self.year} - {self.calculate_amount()} تومان"
