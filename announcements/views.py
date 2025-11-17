from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def announcements_home_view(request):
    return render(request, 'announcements_home.html')
# Create your views here.
