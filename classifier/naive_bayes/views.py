# Create your views here.
from datetime import datetime  # 追加する
from django.http.response import HttpResponse
from django.shortcuts import render # 追加する



def hello_world(request):
    return HttpResponse('Hello World!')

def hello_template(request):
    d = {
        'hour': datetime.now().hour,
        'message': 'Sample message',
    }
    return render(request, 'index.html', d)

def hello_if(request):
    d = {
        'is_visible': False,
        'empty_str': 'hh',
    }
    return render(request, 'if.html', d)

def hello_get_query(request):
    d = {
        'url': request.GET.get('url')
    }
    return render(request, 'get_query.html', d)
