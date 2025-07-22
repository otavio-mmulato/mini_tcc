from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from produtos.models import Produto
from .cart import Cart
from decimal import Decimal

@require_POST
def cart_add(request, product_id):
    """
    Adiciona um produto à sacola a partir da página de detalhes do produto.
    Lê a quantidade do formulário e redireciona para a página da sacola.
    """
    cart = Cart(request)
    product = get_object_or_404(Produto, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    # Aqui usamos override_quantity=False para somar à quantidade existente, se houver.
    # Se quiser que sempre substitua, mude para True.
    cart.add(product=product, quantity=quantity, override_quantity=False)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    """
    Remove um produto da sacola.
    """
    cart = Cart(request)
    product = get_object_or_404(Produto, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    """
    Mostra a página de detalhes da sacola.
    """
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@require_POST
def cart_update(request):
    """
    Atualiza a quantidade de um item via AJAX a partir da página da sacola
    e retorna uma resposta JSON.
    """
    cart = Cart(request)
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))

    product = get_object_or_404(Produto, id=product_id)
    # Aqui usamos override_quantity=True para definir a quantidade exata.
    cart.add(product=product, quantity=quantity, override_quantity=True)

    item_price = Decimal(cart.cart[str(product_id)]['price'])
    item_subtotal = item_price * quantity

    return JsonResponse({
        'status': 'ok',
        'cart_total_price': cart.get_total_price(),
        'cart_total_items': len(cart),
        'item_subtotal': item_subtotal,
    })