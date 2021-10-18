from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Cart, CartItem, Proba, Product1, Cart1, CartItem1
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group, User
from .forms import SignUpForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.views.decorators.http import require_POST


def home(request, category_slug=None):
	category_page = None
	products = None
	if category_slug != None:
		category_page = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=category_page, available=True)
	else:
		products = Product.objects.all().filter(available=True)
	return render(request, 'home.html', {'category':category_page, 'products':products})

def home1(request, proba_slug=None):
	proba_page = None
	products1 = None
	if proba_slug != None:
		proba_page = get_object_or_404(Proba, slug=proba_slug)
		products1 = Product1.objects.filter(proba=proba_page, available=True)
	else:
		products1 = Product1.objects.all().filter(available=True)
	return render(request, 'home1.html', {'proba':proba_page, 'products1':products1})


def product(request, category_slug, product_slug):
	try:
		product = Product.objects.get(category__slug=category_slug, slug=product_slug)
	except Exception as e:
		raise e	
	return render(request, 'product.html', {'product': product})

def product1(request, proba_slug, product1_slug):
	try:
		product1 = Product1.objects.get(proba__slug=proba_slug, slug=product1_slug)
	except Exception as e:
		raise e	
	return render(request, 'product1.html', {'product1': product1})


def _cart_id(request):
	cart = request.session.session_key
	if not cart:
		cart = request.session.create()
	return cart

def _cart_id1(request):
	cart1 = request.session.session_key
	if not cart1:
		cart1 = request.session.create()
	return cart1

def add_cart(request, product_id):
	product = Product.objects.get(id=product_id)
	try:
		cart = Cart.objects.get(cart_id=_cart_id(request))
	except Cart.DoesNotExist:
		cart = Cart.objects.create(cart_id=_cart_id(request))
		cart.save()
	try:
		cart_item = CartItem.objects.get(product=product, cart=cart)
		if cart_item.quantity < cart_item.product.stock:
			cart_item.quantity += 1
		cart_item.save()
	except CartItem.DoesNotExist:
		cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
		cart_item.save()

	return redirect('cart_detail')

def add_cart1(request, product1_id):
	product1 = Product1.objects.get(id=product1_id)
	try:
		cart1 = Cart.objects.get(cart_id=_cart_id(request))
	except Cart.DoesNotExist:
		cart1 = Cart.objects.create(cart_id=_cart_id(request))
		cart1.save()
	try:
		cart_item = CartItem.objects.get(product1=product1, cart1=cart1)
		if cart_item .quantity < cart_item.product1.stock:
			cart_item.quantity += 1
		cart_item.save()
	except CartItem.DoesNotExist:
		cart_item = CartItem.objects.create(product1=product1, quantity=1, cart1=cart1)
		cart_item.save()
	return redirect('cart_detail1')


def cart_detail(request, total=0, counter=0, cart_items=None):
	try:
		cart = Cart.objects.get(cart_id=_cart_id(request))
		cart_items = CartItem.objects.filter(cart=cart, active=True)
		for cart_item in cart_items:
			total += (cart_item.product.price * cart_item.quantity)
			counter += cart_item.quantity
	except ObjectDoesNotExist:
		pass

	return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))

def cart_detail1(request, total1=0, counter1=0, cart_items1=None):
	try:
		cart1 = Cart.objects.get(cart_id1=_cart_id1(request))
		cart_items1 = CartItem1.objects.filter(cart1=cart1, active=True)
		for cart_item1 in cart_items:
			total += (cart_item1.product1.price * cart_item1.quantity)
			counter += cart_item1.quantity
	except ObjectDoesNotExist:
		pass

	return render(request, 'cart1.html', dict(cart_items1=cart_items1, total1=total1, counter1=counter1))


def cart_remove(request, product_id):
	cart = Cart.objects.get(cart_id=_cart_id(request))
	product = get_object_or_404(Product, id=product_id)
	cart_item = CartItem.objects.get(product=product, cart=cart)
	if cart_item.quantity > 1:
		cart_item.quantity -= 1
		cart_item.save()
	else:
		cart_item.delete()
	return redirect('cart_detail')

def cart_remove1(request, product1_id):
	cart1 = Cart.objects.get(cart_id=_cart_id(request))
	product1 = get_object_or_404(Product1, id=product1_id)
	cart_item = CartItem.objects.get(product1=product1, cart1=cart1)
	if cart_item.quantity > 1:
		cart_item.quantity -= 1
		cart_item.save()
	else:
		cart_item.delete()
	return redirect('cart_detail1')

def cart_remove_product(request, product_id):
	cart = Cart.objects.get(cart_id=_cart_id(request))
	product = get_object_or_404(Product, id=product_id)
	cart_item = CartItem.objects.get(product=product, cart=cart)
	cart_item.delete()
	return redirect('cart_detail')

def cart_remove_product1(request, product1_id):
	cart1 = Cart.objects.get(cart_id=_cart_id(request))
	product1 = get_object_or_404(Product1, id=product1_id)
	cart_item = CartItem.objects.get(product1=product1, cart1=cart1)
	cart_item.delete()
	return redirect('cart_detail1')

def signUpView(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username =form.cleaned_data.get('username')	
			signup_user = User.objects.get(username=username)
			user_group = Group.objects.get(name='User')
			user_group.user_set.add(signup_user)
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})

def loginView(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST) 
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				return redirect('signup')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form': form})

def loginView1(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST) 
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home1')
			else:
				return redirect('signup')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form': form})


def signoutView(request):
	logout(request)
	return redirect('login')