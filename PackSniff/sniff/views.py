#a view is a simple function that returns some html
from django.http import HttpResponse
from .models import Packet as PacketModel

def index(request):
    all_IPs = PacketModel.objects.all()
    html = ''
    for IPs in all_IPs:
        url = '/sniff/' 
        html += '<a href="' + url  + '</a><br>'
    return HttpResponse('<h1>This is the IP sniffer app homepage<h1>')
    
def detail(request, ip_address):
    return HttpResponse('<h2>Details for IP Address: ' + str(ip_address) + '</h2>')