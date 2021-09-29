from pro_1.settings import TEMPLATES
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testfun(request):
    # print('heloooooo')
    return HttpResponse('helooo baabte')