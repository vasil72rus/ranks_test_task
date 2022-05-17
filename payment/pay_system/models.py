from django.db import models

class Item(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f'Заказ номер {self.pk}'