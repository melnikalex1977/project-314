from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('1/', views.home1, name='home1'),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.product, name='product_detail'),
    path('proba/<slug:proba_slug>', views.home1, name='products1_by_proba'),
    path('proba/<slug:proba_slug>/<slug:product1_slug>', views.product1, name='product1_detail'),
    
    path('account/create/', views.signUpView, name='signup'),
    path('account/login/', views.loginView, name='login'),
    path('account/login/', views.loginView1, name='login'),
    path('account/signout/', views.signoutView, name='signout'),
    
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),
    path('cart1/remove_product1/<int:product1_id>', views.cart_remove_product1, name='cart_remove_product1'),
    
    path('cart1/remove/<int:product1_id>', views.cart_remove1, name='cart_remove1'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),    
    path('cart1/add/<int:product1_id>', views.add_cart1, name='add_cart1'),
    path('cart1', views.cart_detail1, name='cart_detail1'),
    path('cart', views.cart_detail, name='cart_detail'),
]