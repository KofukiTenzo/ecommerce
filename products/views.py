from tempfile import template
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
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
        products = Products.objects.filter(**request.query_params.dict())
    else:
        products = Products.objects.all()
 
    # if there is something in products else raise error
    if products:
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def add_product(request):
    product = ProductsSerializer(data=request.data)
 
    # validating for already existing data
    if Products.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if product.is_valid():
        product.save()
        return Response(product.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_product(request, pk):
    product = Products.objects.get(pk=pk)
    data = ProductsSerializer(instance=product, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return Response(status=status.HTTP_202_ACCEPTED)