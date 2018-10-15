from django.shortcuts import render

# Create your views here.

def index(request):
    tpl = "sassapp/index.html"
    return render(request, tpl)
