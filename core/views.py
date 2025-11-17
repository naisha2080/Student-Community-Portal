from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#decorator checks if the user is logged in before running the function

@login_required
def home_view(request):
    return render(request, 'home.html')

# Create your views here.
