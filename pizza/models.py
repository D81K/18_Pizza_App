from django.db import models


# Create your models here.

class Size(models.Model):
    name = models.CharField(max_length=6)
    
    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    topping = models.ManyToManyField(Topping)

    def __str__(self):
        toppings = ', '.join(str(v) for v in self.topping.all())
        return f'{self.id} {self.size.name} - {toppings}'

