from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobs(request):
    s='hyderabad jobs information'
    return HttpResponse(s)

def chennaijobs(request):
    s = 'chennai jobs information'
    return HttpResponse(s)
def mumbaijobs(request):
    s='mombai jobs information'
    return HttpResponse(s)
def punejobs(request):
    s='pune jobs information'
    return HttpResponse(s)