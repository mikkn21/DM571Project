from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {"arr": [1,2,3,4]}
    return HttpResponse(render(request, "website/schedule.html", context))

def test(request):
    return HttpResponse("test")

