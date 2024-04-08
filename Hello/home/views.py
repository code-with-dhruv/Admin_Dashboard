from django.shortcuts import render,redirect
from .models import Product,Order,Customer,Tags,Room,Message,Project,Supplier
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
     
    sales1=Product.objects.all()
    sales=sum(product.price for product in sales1)
    orde1=Order.objects.all()
    sale=sales*0.001
    dum=20
    
    mess = Message.objects.order_by('-date').first()
    mess2 = Message.objects.filter(pk__lt=mess.pk).latest('pk')
    mess3 = Message.objects.filter(pk__lt=mess2.pk).latest('pk')

    context={
        "orde1":orde1,
        "sales":sales,
        "mess":mess,
        "mess2":mess2,
        "mess3":mess3,
        "sale":sale,
        "dum":dum
    }
    
    return render(request, 'index.html',context)

def customers(request):
    cust=Customer.objects.all()
    context={
        "cust":cust
    }
    return render(request, 'customers.html',context)
def orders(request):
    orde=Order.objects.all()
    context={
        "orde":orde
    }
    
    return render(request, 'orders.html',context)
def analytics(request):
    item=Project.objects.all()
    context={
        "item":item
    }
    return render(request, 'analytics.html',context)
def messages(request):
    
    return render(request, 'messages.html')
def products(request):
    item=Product.objects.all()
    context={
        "item":item
    }
    
    return render(request, 'products.html',context)
def reports(request):
     
    return render(request, 'reports.html')
def settings(request):
    item=Supplier.objects.all()
    context={
        "item":item
    }
    
    return render(request, 'settings.html',context)
def addproduct(request):
    
    return render(request, 'addproduct.html')
def login(request):
    
    return render(request, 'login.html')
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
