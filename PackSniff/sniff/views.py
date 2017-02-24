#a view is a simple function that returns some html
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>This is the IP sniffer app homepage<h1>')
    
def detail(request, ip_address):
    return HttpResponse('<h2>Details for IP Address: ' + str(ip_address) + '</h2>')