# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse # Not strictly needed here but in image
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})