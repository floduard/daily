from django.db import models


CATEGORY_CHOICES = (
    ('G', 'Ghee'),
    ('CL', 'ChickenLeg'),
    ('CW', 'ChickenWings'),
    ('C', 'Chicken'),
    ('M', 'MilkShake'),
    ('F', 'Fish'),
    ('B', 'Beef'),
    ('E', 'Eggs'),
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField(null=True, blank=True)
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')



    def __str__(self):
        return self.title