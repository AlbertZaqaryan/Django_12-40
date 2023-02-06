from django.shortcuts import render
from .models import Human
# Create your views here.

def home(request):
    human_list = Human.objects.all()
    return render(request, 'users/index.html', context={'human_list':human_list})