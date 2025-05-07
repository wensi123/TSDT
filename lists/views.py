from django.shortcuts import render, redirect
from django.http import HttpResponse # Not strictly needed here but in image
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-new-page/') # This logic is now in new_list
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})