from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.
def profile(request):
    pass
    return HttpResponse("profile")

def index(request):
    pass
    return HttpResponse("blog index")

def post(request,post_slug):
    pass
    return HttpResponse(f"<h1>{post_slug}</h1>")