from django.shortcuts import render

# Create your views here.
def posts(request):
    return render(request, 'posts/posts.html')