from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import LostFoundItem
from .forms import LostFoundForm

@login_required
def lost_found_home_view(request):
    form = LostFoundForm()
    #handles the "Post a New Item" form
    if request.method == 'POST':
        form = LostFoundForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit = False)
            item.author = request.user
            item.save()
            return redirect('lost_found_home')
        else:
            #for a GET request (just loading the page)
            form = LostFoundForm()

    all_items = LostFoundItem.objects.all().order_by('-created_at')

    context = {
            'form': form,
            'all_items': all_items,
        }

    return render(request, 'lost_found_home.html', context)

@login_required
def lost_found_delete_view(request, pk):
    #get the specific item
    item = get_object_or_404(LostFoundItem, pk=pk)
    if item.author == request.user and request.method == 'POST':
        if item.image:
            item.image.delete()
        item.delete()

    return redirect('lost_found_home')

@login_required   
def lost_found_claim_view(request, pk):
    item = get_object_or_404(LostFoundItem, pk=pk)
    if item.author == request.user and request.method == 'POST':
        item.is_claimed = True
        item.save()
    
    return redirect('lost_found_home')
# Create your views here.
