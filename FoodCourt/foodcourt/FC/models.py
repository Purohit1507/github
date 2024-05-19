from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Bread', 'Bread Items'),
        ('Punjabi', 'Punjabi Items'),
        ('SouthIndian', 'South Indian Items'),
        ('NonVeg', 'Non Veg Items'),
        ('Beverages', 'Beverages'),
        ('Extra', 'Extra Items'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.price}'

class Order(models.Model):
    name = models.CharField(max_length=100)
    ps_no = models.IntegerField()
    dept_shop = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    date = models.DateField()
    break_time = models.TimeField()
    items = models.ManyToManyField(MenuItem, through='OrderItem')

    def __str__(self):
        return f'Order by {self.name} on {self.date}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class DayMenu(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    day = models.CharField(max_length=9, choices=DAY_CHOICES, unique=True)
    items = models.ManyToManyField(MenuItem)

    def __str__(self):
        return self.day
    
class PunjabiItems(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.item_name} - {self.price}'
