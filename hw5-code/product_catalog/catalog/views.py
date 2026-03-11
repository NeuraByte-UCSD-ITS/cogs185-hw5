from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.contrib import messages

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item added successfully!')
            return redirect('list_items')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

def list_items(request):
    items = Item.objects.all().order_by('-created_at')
    return render(request, 'list_items.html', {'items': items})
