import urllib2
from pickle import load
saved  = open('out', 'rb')
hosts  = load(saved)

for mantaops_cookie in hosts['mantaops.com/']:
	opener = urllib2.build_opener()
	opener.addheaders.append(('Cookie',mantaops_cookie))
	body = urllib2.urlopen("http://mantaops.com/").read()
	print body.decode("cp1251")