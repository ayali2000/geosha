from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q, query
from store.models import Product
from . form import OrderForm
from django.core.paginator import Paginator

# Create your views here.
def products(request):
    prods = Product.objects.all()
    query = request.GET.get('q','')
    paginator = Paginator(prods,20)
    page = request.GET.get('pg')
    prods = paginator.get_page(page)
    if query:
        queryset=(Q(productname__icontains=query))
        results=Product.objects.filter(queryset).distinct()
    else:
        results=[]
    context = {
        "prods":prods,
        "query":query,
        "results":results
    }
    return render(request,'store/products.html',context)


def order(request,pk):
    item = Product.objects.get(pk=pk)
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item orderd.') 
            return redirect("order",pk=item.id)
        else:
            form = OrderForm()    
    context = {
        "item":item,
        "form":form
    }     
    return render(request,"store/order.html",context)
    