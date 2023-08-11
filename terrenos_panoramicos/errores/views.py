from django.shortcuts import render
from django.http import HttpResponseForbidden

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_403_view(request, exception):
    return HttpResponseForbidden(render(request, '403.html', status=403))
