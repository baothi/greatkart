from django.shortcuts import render
from store.models import Product


# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id) # get the product
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) #get the cart using the cart_id persent in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()


def cart(request):
    return render(request, 'store/cart.html')
