from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Product

def index(request):

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'mainapp/index.html', context)

@csrf_exempt
def post(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        price = request.POST.get('price', '')
        product = Product(name=name, description=description, price=price)
        product.save()
        json = {
            'id': product.id,
            'name': name,
        }
        return JsonResponse(json)

@csrf_exempt
def delete(request, id):
    if request.method == "DELETE":
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponse("Success")

@csrf_exempt
def details(request, id):
    if request.method == "GET":
        product = Product.objects.get(id=id)
        productDetails = {}
        productDetails['id'] = product.id
        productDetails['name'] = product.name
        productDetails['desc'] = product.description
        productDetails['price'] = product.price
        return JsonResponse(productDetails)

@csrf_exempt
def update(request, id):
    if request.method == "PUT":
        product = Product.objects.get(id=id)
        put = QueryDict(request.body)
        product.name = put.get('name')
        product.description = put.get('description')
        product.price = put.get('price')
        product.save()
        json = {
            'id': product.id,
            'name': product.name,
        }
        return JsonResponse(json)
