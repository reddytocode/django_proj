#django
from django.http import HttpResponse
#utilities
from datetime import datetime

def hello(request):
    now = datetime.now().strftime('%b %dth')
    return HttpResponse('Hello, it\'s: {}'.format(now))

def hi(request):
    return HttpResponse('Hi')