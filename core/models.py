from django.conf import settings
from django.db import models
from django.shortcuts import reverse

# Create your models here.

CATEGORY_CHOICES = (
    ('R', 'Regular'),
    ('J', 'Jumbo'),
    ('S', 'Special')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    # linkes Item and Order
    # Item becomes OrderItem when you add it to cart
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Order(models.Model):
    # shopping cart
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username
