from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='category', blank=True)

	class Meta:
		ordering =('name', )
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_url(self):
		return reverse('products_by_category', args=[self.slug])

	def __str__(self):
			return self.name

class Proba(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='proba', blank=True)

	class Meta:
		ordering =('name', )
		verbose_name = 'proba'
		verbose_name_plural = 'probas'

	def get_url(self):
		return reverse('products1_by_proba', args=[self.slug])

	def __str__(self):
			return self.name



class Product(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='product', blank=True)
	stock = models.IntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering =('name', )
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def get_url(self):
		return reverse('product_detail', args=[self.category.slug, self.slug])

	def __str__(self):
			return self.name

class Product1(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	proba = models.ForeignKey(Proba, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='product1', blank=True)
	stock = models.IntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering =('name', )
		verbose_name = 'product1'
		verbose_name_plural = 'products1'

	def get_url(self):
		return reverse('product1_detail', args=[self.proba.slug, self.slug])

	def __str__(self):
			return self.name

class Cart(models.Model):
	cart_id = models.CharField(max_length=250, blank=True)
	date_added = models.DateField(auto_now_add=True)
	class Meta: 
		ordering = ['date_added']
		db_table = 'Cart'

	def __str__(self):
			return self.cart_id

class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	active = models.BooleanField(default=True)

	class Meta:
		db_table = 'CartItem'

	def sub_total(self):
		return self.product.price * self.quantity

	def __str__(self):
			return self.product

	def sub_total1(self):
		return self.product1.price * self.quantity

	def __str__1(self):
			return self.product1





