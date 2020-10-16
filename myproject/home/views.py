from django.shortcuts import render
from .models import FoodItem,Contact,Order
from math import ceil
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):

    allitems=[]
    cat_items= FoodItem.objects.values('category','id')
    cats={itemm['category'] for itemm in cat_items }
    for cat in cats:
        itm=FoodItem.objects.filter(category=cat)
        n=len(itm)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allitems.append([itm,range(1,nSlides),nSlides])
    params = {'allitems': allitems}

    return render(request,'index.html',params)



def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        feedback = request.POST.get('feedback')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,feedback=feedback,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')



def order(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        order = Order(items_json=items_json, name=name, email=email, address=address, city=city, state=state,
                       zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'order.html', {'thank': thank, 'id': id})
    return render(request, 'order.html')
