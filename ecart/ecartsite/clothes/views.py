from django.shortcuts import render,get_object_or_404,redirect
from .models import clothes

def clothes_list(request):
    pavan=clothes.objects.all()
    return render(request,'clothes.html',{'clot':pavan})
def product_add(request): 
    if request.method == 'POST': 
    
        product_id = request.POST.get('product_id') 
        name = request.POST.get('name') 
        customer_id = request.POST.get('customer_id') 
        price = request.POST.get('price') 
        clothes.objects.create(
            product_id=product_id, 
            name=name, 
            customer_id=customer_id, 
            price=price 
        ) 
        return redirect('clothes')
    return render(request, 'clo.html')





