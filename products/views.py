from tempfile import template
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Products
from .serializer import ProductsSerializer

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_products': '/',
        'Search by Name': '/?name=name',
        'Search by Category': '/?category=category_name',
        'Search by Rate': '/?rate=rate_amount',
        'Search by Price': '/?price=price_amount',
        'Add': '',
        'Update': '',
        'Delete': ''
    }
 
    return Response(api_urls)

@api_view(['GET'])
def view_products(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Products.objects.filter(**request.query_params.dict())
    else:
        items = Products.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = ProductsSerializer(items, many=True)
        return Response({"products" : serializer.data}, template="templates\homepage\index.html")
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)