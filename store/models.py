from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):                                                                 #Customer's data is stored here
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return str(self.user)


class Product(models.Model):            #Product data
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    product_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def product_imageURL(self):
        try:
            url = self.product_image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)              #foreign key relates Order to Customer
    date_ordered = models.DateTimeField(auto_now_add=True)                                                #as Many to One relationship
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.product_total for item in orderitems])
        return total

    @property
    def get_cart_quantity(self):
        orderitmes = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitmes])
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    @property
    def product_total(self):
        total = self.product.price * self.quantity
        return total


class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


