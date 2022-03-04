from multiprocessing import context
from re import template
from urllib import request
from django.http import HttpResponse, response,Http404,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from shop.models import Product
from django.utils import timezone
from django.template import loader
from .forms import productForm

def index(request):
    listProduct = Product.objects.all()
    template = loader.get_template('shop/index.html')
    form = productForm(request.POST, use_required_attribute=False)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/shop')
    context = {
        'listProduct' : listProduct,
        'form' : form,
    }
    return HttpResponse(template.render(context, request))
    
def create(request):
    form = productForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/shop')
    template = loader.get_template('shop/create.html')
    context = {
        'form': form,

    }
    return HttpResponse(template.render(context, request))
    
def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'shop/detail.html', {'product': product})

def update(request, product_id): 
    product = get_object_or_404(Product, pk=product_id)
    form = productForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/shop')
    template = loader.get_template('shop/update.html')
    context = {
        'form': form,

    }

    return HttpResponse(template.render(context, request))

def delete(request, product_id):
    trash = get_object_or_404(Product, pk=product_id)
    trash.delete()
    return HttpResponseRedirect('/shop')