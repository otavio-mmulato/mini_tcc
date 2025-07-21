from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from produtos.models import Produto
from .cart import Cart

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produto, id=product_id)
    # Por enquanto, adicionaremos sempre 1 unidade
    cart.add(product=product, quantity=1)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produto, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})
# ...
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produto, id=product_id)
    
    # Pega a quantidade do formulário. Se não vier, o padrão é 1.
    quantity = int(request.POST.get('quantity', 1))
    
    cart.add(product=product, quantity=quantity, override_quantity=True) # Usamos override para definir a quantidade exata
    return redirect('cart:cart_detail')
# ...