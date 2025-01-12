from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json

def list_products(request):
    products = list(Product.objects.values('id', 'name', 'price', 'category__name'))
    return JsonResponse({'products': products})

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product = Product.objects.create(
            name=data['name'],
            price=data['price'],
            category_id=data['category_id'],
        )
        return JsonResponse({'id': product.id, 'status': 'Product created successfully'})
