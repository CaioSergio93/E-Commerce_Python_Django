from django.shortcuts import render
from store.models import Product

def product_list(request):
    products = Product.objects.filter(available=True)
    # Formata o preço de cada produto
    for product in products:
        product.price_formatted = f"R$ {product.price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    context = {'products': products}
    return render(request, 'store/product_list.html', context)