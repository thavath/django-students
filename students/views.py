from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'students/index.html', context)

def detail(request):
    context = {}
    return render(request, 'students/detail.html', context)
